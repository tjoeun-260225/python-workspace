from flask import Blueprint, render_template, request, jsonify
from faker import Faker

from db import db
from models import User
import es_client as es_service

routes = Blueprint("routes", __name__)
fake   = Faker("ko_KR")


@routes.get("/")
def index():
    total = User.query.count()
    es_ok = es_service.es.ping()
    return render_template("index.html", total=total, es_ok=es_ok)


@routes.post("/api/seed")
def seed():
    count = int(request.json.get("count", 20))
    added = 0
    for _ in range(count):
        try:
            user = User(
                name    = fake.name(),
                email   = fake.unique.email(),
                phone   = fake.phone_number(),
                job     = fake.job(),
                company = fake.company(),
                city    = fake.city(),
                country = "대한민국",
            )
            db.session.add(user)
            db.session.flush()
            es_service.index_user(user.id, user.to_dict())
            added += 1
        except Exception:
            db.session.rollback()
    db.session.commit()
    fake.unique.clear()
    return jsonify({"added": added, "total": User.query.count()})


@routes.get("/api/users")
def get_users():
    page     = int(request.args.get("page", 1))
    per_page = int(request.args.get("per",  10))
    p = User.query.order_by(User.id.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    return jsonify({
        "users": [u.to_dict() for u in p.items],
        "total": p.total,
        "pages": p.pages,
        "page":  p.page,
    })


@routes.get("/api/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"hits": [], "total": 0})
    return jsonify(es_service.search_users(q))


@routes.get("/api/stats")
def stats():
    try:
        es_count = es_service.count_users()
    except Exception:
        es_count = 0
    return jsonify({"mysql": User.query.count(), "elasticsearch": es_count})


@routes.delete("/api/delete_all")
def delete_all():
    User.query.delete()
    db.session.commit()
    try:
        es_service.delete_all_users()
    except Exception:
        pass
    return jsonify({"ok": True})