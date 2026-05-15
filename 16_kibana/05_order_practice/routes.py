import random
from flask import Blueprint, render_template, request, jsonify
from faker import Faker
from sqlalchemy import func

from db import db
from models import User, Product, Order
import es_client as es_service

routes = Blueprint("routes", __name__)
fake = Faker("ko_KR")

STATUSES = ["결제완료", "배송중", "배송완료", "취소"]

PRODUCT_POOL = [
    ("갤럭시 S24", "전자제품", 1200000, "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400"),
    ("에어팟 프로", "전자제품", 350000, "https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?w=400"),
    ("맥북 프로", "전자제품", 2800000, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
    ("나이키 운동화", "의류", 150000, "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"),
    ("무신사 후드티", "의류", 59000, "https://images.unsplash.com/photo-1556821840-3a63f15732ce?w=400"),
    ("쌀 10kg", "식품", 35000, "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"),
    ("제주 감귤", "식품", 18000, "https://images.unsplash.com/photo-1547514701-42782101795e?w=400"),
    ("파이썬 입문", "도서", 25000, "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400"),
    ("클린 코드", "도서", 30000, "https://images.unsplash.com/photo-1589998059171-988d887df646?w=400"),
    ("요가 매트", "스포츠", 45000, "https://images.unsplash.com/photo-1601925228876-9c5e78be6e23?w=400"),
    ("덤벨 10kg", "스포츠", 38000, "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400"),
    ("공기청정기", "생활용품", 320000, "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400"),
    ("전동 칫솔", "뷰티", 89000, "https://images.unsplash.com/photo-1559591935-c35a5b4a0e2e?w=400"),
    ("레고 시티", "완구", 65000, "https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=400"),
    ("텀블러", "생활용품", 29000, "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=400"),
]


@routes.get("/")
def index():
    products = Product.query.order_by(Product.id).all()
    return render_template("index.html", products=products)


@routes.get("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)


@routes.get("/orders")
def order_list():
    return render_template("order.html")


@routes.post("/api/seed")
def seed():
    count = int(request.json.get("count", 20))

    if Product.query.count() == 0:
        for name, cat, price, img in PRODUCT_POOL:
            db.session.add(Product(name=name, category=cat, price=price, stock=200, image_url=img))
        db.session.commit()

    products = Product.query.all()
    added = 0

    for _ in range(count):
        try:
            user = User(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address().replace("\n", " "),
            )
            db.session.add(user)
            db.session.flush()

            for _ in range(random.randint(1, 4)):
                product = random.choice(products)
                qty = random.randint(1, 5)
                status = random.choice(STATUSES)

                order = Order(
                    user_id=user.id,
                    product_id=product.id,
                    quantity=qty,
                    total_price=product.price * qty,
                    status=status,
                )
                db.session.add(order)
                db.session.flush()

                es_service.index_order(order.id, order.to_dict())
                added += 1

        except Exception as e:
            db.session.rollback()
            print(e)

    db.session.commit()
    fake.unique.clear()
    return jsonify({"added": added, "total": Order.query.count()})


@routes.post("/api/order")
def place_order():
    data = request.json
    product_id = data.get("product_id")
    quantity = int(data.get("quantity", 1))
    user_name = data.get("user_name", "").strip()
    user_email = data.get("user_email", "").strip()

    if not user_name or not user_email:
        return jsonify({"ok": False, "msg": "이름과 이메일을 입력하세요"}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"ok": False, "msg": "상품 없음"}), 404

    if product.stock < quantity:
        return jsonify({"ok": False, "msg": "재고가 부족합니다"}), 400

    user = User.query.filter_by(email=user_email).first()
    if not user:
        user = User(name=user_name, email=user_email)
        db.session.add(user)
        db.session.flush()

    order = Order(
        user_id=user.id,
        product_id=product.id,
        quantity=quantity,
        total_price=product.price * quantity,
        status="결제완료",
    )
    db.session.add(order)

    product.stock -= quantity
    db.session.flush()

    es_service.index_order(order.id, order.to_dict())

    db.session.commit()
    return jsonify({"ok": True, "order_id": order.id, "total": order.total_price})


@routes.delete("/api/delete_all")
def delete_all():
    Order.query.delete()
    User.query.delete()
    Product.query.delete()
    db.session.commit()
    try:
        es_service.delete_all()
    except Exception:
        pass
    return jsonify({"ok": True})


@routes.get("/api/products")
def get_products():
    products = Product.query.order_by(Product.id).all()
    return jsonify([p.to_dict() for p in products])


@routes.get("/api/orders")
def get_orders():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per", 10))

    p = Order.query.order_by(Order.id.desc()).paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "orders": [o.to_dict() for o in p.items],
        "total": p.total,
        "pages": p.pages,
        "page": p.page,
    })


@routes.get("/api/stats")
def stats():
    try:
        es_count = es_service.count()
    except Exception:
        es_count = 0

    status_rows = db.session.query(Order.status, func.count()).group_by(Order.status).all()
    status_map = {s: c for s, c in status_rows}

    category_rows = (
        db.session.query(Product.category, func.sum(Order.total_price))
        .join(Order, Order.product_id == Product.id)
        .group_by(Product.category)
        .all()
    )
    category_sales = {cat: int(total or 0) for cat, total in category_rows}

    return jsonify({
        "total_orders": Order.query.count(),
        "total_users": User.query.count(),
        "total_products": Product.query.count(),
        "elasticsearch": es_count,
        "status": status_map,
        "category_sales": category_sales,
    })


@routes.get("/api/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"hits": [], "total": 0})
    return jsonify(es_service.search_orders(q))
