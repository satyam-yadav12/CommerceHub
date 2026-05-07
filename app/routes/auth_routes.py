from flask import Blueprint, jsonify
from ..extensions import db
from sqlalchemy import text

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/healthz", methods=["GET"])
def check_health():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"msg": "database connected successfully"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)})
