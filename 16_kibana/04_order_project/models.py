from db import db

class User(db.Model):
    __tablename__ = "users"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(150), unique=True, nullable=False)
    phone      = db.Column(db.String(30))
    address    = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    orders     = db.relationship("Order", backref="user", lazy=True)

    def to_dict(self):
        return {
            "id":         self.id,
            "name":       self.name,
            "email":      self.email,
            "phone":      self.phone,
            "address":    self.address,
            "created_at": str(self.created_at),
        }


class Product(db.Model):
    __tablename__ = "products"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    category   = db.Column(db.String(50))
    price      = db.Column(db.Integer, nullable=False)   # 원 단위
    stock      = db.Column(db.Integer, default=100)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            "id":         self.id,
            "name":       self.name,
            "category":   self.category,
            "price":      self.price,
            "stock":      self.stock,
            "created_at": str(self.created_at),
        }


class Order(db.Model):
    __tablename__ = "orders"

    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity   = db.Column(db.Integer, default=1)
    total_price= db.Column(db.Integer)                   # quantity * price
    status     = db.Column(db.String(20), default="결제완료")  # 결제완료/배송중/배송완료/취소
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    product    = db.relationship("Product", lazy=True)

    def to_dict(self):
        return {
            "id":          self.id,
            "user_id":     self.user_id,
            "user_name":   self.user.name if self.user else "",
            "product_id":  self.product_id,
            "product_name":self.product.name if self.product else "",
            "category":    self.product.category if self.product else "",
            "quantity":    self.quantity,
            "total_price": self.total_price,
            "status":      self.status,
            "created_at":  str(self.created_at),
        }