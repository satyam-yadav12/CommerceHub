from ...models.product_details import ProductCategories, Product
from ...extensions import db
from ..responses.errors import ApiError


def add_category_db(category):
    obj = ProductCategories(category_name = category)
    try:
        db.session.add(obj)
        db.session.commit()
        return obj.id
    except Exception as e:
        return ApiError(500, "Unable to perform required action", "Server Error")

def add_product_db(data):
    obj = Product(data)
    try:
            db.session.add(obj)
            db.session.commit()
            return obj.id
    except Exception as e:
            db.session.rollback()
            return ApiError(500, "Unable to perform required action", "Server Error")