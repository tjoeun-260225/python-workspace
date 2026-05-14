from db import db

class User(db.Model):
    __tablename__ = "users"

    id         = db.Column(db.Integer,     primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(150), unique=True, nullable=False)
    phone      = db.Column(db.String(30))
    job        = db.Column(db.String(100))
    company    = db.Column(db.String(100))
    city       = db.Column(db.String(100))
    country    = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self) -> dict:
        return {
            "id":         self.id,
            "name":       self.name,
            "email":      self.email,
            "phone":      self.phone,
            "job":        self.job,
            "company":    self.company,
            "city":       self.city,
            "country":    self.country,
            "created_at": str(self.created_at),
        }