from flask import Blueprint, jsonify
from ..extensions import db
from sqlalchemy import text
from ..responses.success import create_success_response

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/healthz", methods=["GET"])
def check_health():
    try:
        db.session.execute(text("SELECT 1"))
        return create_success_response(
            200,
            "sql connected successfully",
        )
    except Exception as e:
        raise Exception(e)


@auth_bp.route("/check", methods=["GET"])
def check_route():
    try:
        return create_success_response(200, "response created successfull")
    except Exception as e:
        raise Exception(e)
