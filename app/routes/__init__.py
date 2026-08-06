from flask import Blueprint, jsonify, request
from ..extensions import db
from sqlalchemy import text
from ..utils.responses.success import create_success_response

test_bp = Blueprint("test", __name__)


@test_bp.route("/healthz", methods=["GET"])
def check_health():
    try:
        db.session.execute(text("SELECT 1"))
        return create_success_response(
            200,
            "sql connected successfully",
        )
    except Exception as e:
        raise Exception(e)


@test_bp.route("/check", methods=["GET"])
def check_route():
    try:
        return create_success_response(200, "response created successfull")
    except Exception as e:
        raise Exception(e)


@test_bp.route("/upload_product", methods=["POST"])
def upload_product_img():
    pass


@test_bp.route("/delete_product/<id>", methods=["DELETE"])
def delete_product_img(id):
    pass
