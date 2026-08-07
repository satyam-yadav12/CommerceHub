from flask import request, jsonify, request
from ..utils.responses.success import create_success_response
from ..services.admin_services import (
    register_admin_service,
    admin_login_service,
    add_product_service,
  add_product_variant_service
)
from flask_jwt_extended import set_access_cookies
import random
import string, re, time
from ..utils.responses.errors import ApiError
from ..utils.cloudinary.cloudinary_services import (
    upload_product_image_cloudinary,
    destroy_product_image,
)
from ..utils.database.product_operations_database import (
    add_category_db,
    fetch_products_list_db,
    fetch_single_product,
)

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


# admin product operations


def upload_product_image():  # TODO: move logic to service
    img = request.files.get("product_image")
    if not img:
        raise ApiError(400, "file not uploaded", "Invalid Data")

    if img and img.filename and img.filename.strip() != "":
        raise ApiError(400, "file not uploaded", "Invalid Data")

    filename = img.filename
    safe = re.sub(r"[^a-zA-Z0-9]", "", filename)
    safe = safe[:10].lower()

    word = f"{safe}_{int(time.time())}"

    response = upload_product_image_cloudinary(img, word)
    #FIXME: NO DB OPERATION WRITTEN FOR THIS FUNCTION YET
    if response:
        return create_success_response(201, "file upload success", response)

"""
{
        "msg": "image uploaded successfull",
        "uri": upload_results["secure_url"],
        "thumb_uri" : thumbUrl,
        "img_height": upload_results["height"],
        "img_width": upload_results["width"],
        "public_id": upload_results["public_id"],
        "folder": "commerce_hub",
    }
"""

def add_product_category():
    data = request.get_json()
    category = data.get('category_name')
    if not category:
        return ApiError(400, "category name required", "Invalid data")

    #TODO: move this code to service layer
    result = add_category_db(category)
    if not result:
        return ApiError(500, "Unexpected Error Occured", "Server Error")
    return create_success_response(201, "category added successful", result)

def add_product_variant_controller(): #FIXME: half written
    data = request.get_json()
    required = {"variant_name": data.get("variant_name"),
                "color" : data.get("color"),
                "size" : data.get('size'),
                "weight" : data.get('weight'),
                "product_id": data.get("product_id"),
                " stock_quantity": data.get("stock"),
                'price':data.get("price") 
                }
    result = add_product_variant_service(required)


  
    return create_success_response(201, "product added successful", result)

def delete_product_image():  # FIXME: function does not get correct public_id for cloudinary Image
    response = destroy_product_image(id)
    return create_success_response(204, "file deleted successful", response)


def add_product_controller():
    data = request.get_json()

    required = {"title" : data.get("title"), "description": data.get("description"), "category": data.get('category_id')}
    result = add_product_service(required)

    return create_success_response(201, "product added successfully", result)


def fetch_all_products_controller(category):
    
    # admin authentication logic
    # fetch products service
    # fetch products db logic
    result  = fetch_products_list_db(category)
    # prepare data to show
    return create_success_response(200, "product fetch successsul", result)

def fetch_product_with_id(product_id):
    #admin authentication logic
    #fetch products services
    #fetch product db logic
    result  = fetch_single_product(product_id)

    #prepare data to show
    return  create_success_response(200, "product fetch successfully", result)
