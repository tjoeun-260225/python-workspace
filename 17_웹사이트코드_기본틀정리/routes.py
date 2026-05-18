import random
from sys import exc_info

from flask import Blueprint, render_template, request, jsonify
from faker import Faker
from jieba import total

from db import db
from models import User, Product, Order
import es_client as es_service

""" API 에 로그 추가 """
from logger import get_logger  # 1. 우리가 만든 get_logger 사용

routes = Blueprint("routes", __name__)
fake = Faker("ko_KR")
log = get_logger("routes")  # 2. 로그 변수 생성

CATEGORIES = ["전자제품", "의류", "식품", "도서", "스포츠", "생활용품", "뷰티", "완구"]
STATUSES = ["결제완료", "배송중", "배송완료", "취소"]

PRODUCT_POOL = [
    ("갤럭시 S24", "전자제품", 1200000),
    ("에어팟 프로", "전자제품", 350000),
    ("나이키 운동화", "의류", 150000),
    ("무신사 후드티", "의류", 59000),
    ("쌀 10kg", "식품", 35000),
    ("참치캔 세트", "식품", 18000),
    ("파이썬 입문 책", "도서", 25000),
    ("클린 코드", "도서", 30000),
    ("요가 매트", "스포츠", 45000),
    ("덤벨 10kg", "스포츠", 38000),
    ("가습기", "생활용품", 75000),
    ("전동 칫솔", "뷰티", 89000),
    ("레고 시티", "완구", 65000),
    ("텀블러", "생활용품", 29000),
    ("무선 마우스", "전자제품", 42000),
]


# 메인 페이지
@routes.get("/")
def index():
    total_orders = Order.query.count()
    total_users = User.query.count()
    total_products = Product.query.count()
    log.info("메인 페이지 접속", extra={"x_total_orders": total_orders})
    return render_template(
        "index.html",
        total_orders=total_orders,
        total_users=total_users,
        total_products=total_products,
    )


# 더미 데이터 생성
@routes.post("/api/seed")
def seed():
    count = int(request.json.get("count", 20))
    log.info("더미 데이터 생성 시작", extra={"x_count": count})  # x_count 이름으로 count 작성하겠다.
    # 1) 상품 없으면 미리 넣기
    if Product.query.count() == 0:
        for name, cat, price in PRODUCT_POOL:
            db.session.add(Product(name=name, category=cat, price=price, stock=200))
        db.session.commit()

    products = Product.query.all()

    # 2) 유저 + 주문 생성
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

            # 유저 한 명당 1~3개 주문
            for _ in range(random.randint(1, 3)):
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
            # print(e) log 보다 느리고, log 파일로 기록할 수 없는 일회성 출력으로 회사에서는 배포용으로 사용 안함
            log.error("유저/주문 생성 실패", extra={"x_error": str(e)}, exc_info=True)
    db.session.commit()
    fake.unique.clear()

    total = Order.query.count()
    log.info("더미 데이터 생성 완료", extra={"x_added": added, "x_total": total})
    return jsonify({"added": added, "total": Order.query.count()})


# 전체 삭제
@routes.delete("/api/delete_all")
def delete_all():
    log.warning("전체 데이터 삭제 요청")
    Order.query.delete()
    User.query.delete()
    Product.query.delete()
    db.session.commit()
    try:
        es_service.delete_all_orders()
    except Exception as e:
        log.error("ES 데이터 삭제 실패", extra={"x_error": str(e)}, exc_info=True)
        # pass
    log.warning("전체 데이터 삭제 완료")
    return jsonify({"ok": True})


# 통계
@routes.get("/api/stats")
def stats():
    try:
        es_count = es_service.count_orders()
    except Exception as e:
        log.error("ES 카운트 조회 실패", extra={"x_error": str(e)})
        es_count = 0

    # 상태별 집계
    from sqlalchemy import func
    status_rows = db.session.query(Order.status, func.count()).group_by(Order.status).all()
    status_map = {s: c for s, c in status_rows}

    result = {
        "mysql_orders": Order.query.count(),
        "mysql_users": User.query.count(),
        "mysql_products": Product.query.count(),
        "elasticsearch": es_count,
        "status": status_map,
    }

    log.info("통계 조회", extra={"x_mysql_ordes": result["mysql_orders"], "x_es_count": es_count})
    return jsonify(result)


# 주문 목록 (페이징)
@routes.get("/api/orders")
def get_orders():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per", 10))
    p = Order.query.order_by(Order.id.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    log.info("주문 목록 조회", extra={"x_page": page, "x_total": p.total})
    return jsonify({
        "orders": [o.to_dict() for o in p.items],
        "total": p.total,
        "pages": p.pages,
        "page": p.page,
    })


# MySQL 주문 검색
@routes.get("/api/mysql_search")
def mysql_search():
    q = request.args.get("q", "").strip()
    log.info("MySQL 검색 요청", extra={"x_query": q})
    if not q:
        return jsonify({"orders": [], "total": 0})
    like = f"%{q}%"
    results = (
        Order.query
        .join(User, Order.user_id == User.id)
        .join(Product, Order.product_id == Product.id)
        .filter(
            db.or_(
                User.name.like(like),
                Product.name.like(like),
                Product.category.like(like),
                Order.status.like(like),
            )
        )
        .order_by(Order.id.desc())
        .limit(50)
        .all()
    )
    log.info("MySQL 검색 완료", extra={"x_query": q, "x_hits": len(results)})
    return jsonify({"orders": [o.to_dict() for o in results], "total": len(results)})


# ES 검색
@routes.get("/api/search")
def search():
    q = request.args.get("q", "").strip()
    log.info("ES 검색 요청", extra={"x_query": q})
    if not q:
        return jsonify({"hits": [], "total": 0})
    result = es_service.search_orders(q)

    log.info("ES 검색 완료", extra={"x_query": q, "x_hits": result["total"]})
    return jsonify(result)
