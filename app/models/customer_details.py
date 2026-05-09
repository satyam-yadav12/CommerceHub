from ..extensions import db


class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(40), nullable=False)
    contact = db.Column(db.String(20), unique=True)
    addresses = db.relationship("Addresses", backref="customer", lazy=True)
    orders = db.relationship("Orders", backref="order")


class Addresses(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(50), nullable=False)
    town = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(40), nullable=False)
    pin_code = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    is_default = db.Column(db.Boolean, default=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
