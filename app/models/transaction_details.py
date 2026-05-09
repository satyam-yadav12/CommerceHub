from ..extensions import db
from sqlalchemy import func


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    transaction_amount = db.Column(db.Numeric(10, 2), nullable=False)
    method = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
