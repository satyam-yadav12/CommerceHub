from flask import request, jsonify
from ..utils.responses.success import create_success_response
from ..services.admin_services import register_admin_service, admin_login_service
from flask_jwt_extended import set_access_cookies


def register_admin_controller():
    data = request.get_json()

    required = {"email": data.get("email"), "password": data.get("password")}
    response = register_admin_service(required)

    return create_success_response(201, "admin registered successfully", response)


def admin_login_controller():
    data = request.get_json()

    required = {"email": data.get("email"), "password": data.get("password")}
    result = admin_login_service(required)

    response = jsonify({"message": "login successfull"})

    set_access_cookies(response, result["access_token"])
    return response, 200
