from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.database.admin_database import add_admin_data, get_user_data
from ..utils.responses.errors import ApiError
from flask_jwt_extended import create_access_token


def register_admin_service(data):  # TODO: Test the Function Logic
    if not data["username"] or not data["password"]:
        raise ApiError(400, "Username and password required", "Invalid data")
    hash = generate_password_hash(data["password"])
    user = {"username": data["username"], "password": hash}
    response = add_admin_data(user)
    print(response)
    return None


def admin_login_service(data):  # TODO: test the function through PostMan
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

"""
 {"title" : data.get("title"), 
 "description": data.get("description"),
   "category": data.get('category_id')}
"""
def add_product_service(data):  # TODO: complete the function

    parsed_data = prepare_img_data(data)

    result = add_product_db(parsed_data)
    
    return result


def prepare_img_data(data):
  
    product = {
        "product_title": data.get("title"),
        "product_description": data.get("description"),
        "category_id":data.get("category"),
    }
    return product
