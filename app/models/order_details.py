from ..extensions import db
from sqlalchemy.sql import func


class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    order_items = db.relationship("OrderItems", backref="item")
    order_status = db.Column(db.String(20), nullable=False, default="Order Placed")
    transaction_id = db.relationship("Transactions", backref="transaction")
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    amount = db.Column(db.Numeric(10, 2), nullable=False)


class OrderItems(db.Model):
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(
        db.Integer, db.ForeignKey("product_variants.id"), nullable=False
    )
    quantity = db.Column(db.Integer, default=1, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    price_at_purchase = db.Column(db.Numeric(10, 2), nullable=False)
