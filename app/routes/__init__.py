from flask import Blueprint, jsonify, request
from ..extensions import db
from sqlalchemy import text
from ..utils.responses.success import create_success_response
import random
import string
from ..utils.responses.errors import ApiError
from ..utils.cloudinary.cloudinary_services import (
    upload_product_image,
    destroy_product_image,
)

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

    file = request.files.get("product_image")
    if not file:
        raise ApiError(400, "file not uploaded", "Invalid Data")

    word = "".join(random.choices(string.ascii_lowercase, k=6))

    response = upload_product_image(file, word)

    if response:
        return create_success_response(201, "file upload success", response)


@test_bp.route("/delete_product/<id>", methods=["DELETE"])
def delete_product_img(id):
    response = destroy_product_image(id)
    return create_success_response(204, "file deleted successful", response)
