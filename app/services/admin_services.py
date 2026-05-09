from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.database.admin_database import add_admin_data, get_user_data
from ..utils.responses.errors import ApiError
from flask_jwt_extended import create_access_token


def register_admin_service(data):
    if not data["username"] or not data["password"]:
        raise ApiError(400, "Username and password required", "Invalid data")
    hash = generate_password_hash(data["password"])
    user = {"username": data["username"], "password": hash}
    response = add_admin_data(user)
    print(response)
    return None


def admin_login_service(data):
    if not data["username"] or not data["password"]:
        raise ApiError(400, "Username and password required", "Invalid data")

    result = get_user_data(data["username"])
    compare_pass = check_password_hash(result["password"], data["password"])
    if not compare_pass:
        raise ApiError(400, "Invalid Password", "Invalid data")

    id = result["username"]
    additional = {"role": "admin"}
    access_token = create_access_token(id, additional_claims=additional)

    response = {"username": data["username"], "access_token": access_token}
    return response
