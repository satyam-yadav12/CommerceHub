from ...models.product_details import ProductVariants, ProductCategories, Product, ProductImages
from ...extensions import db
from ..responses.errors import ApiError
from sqlalchemy import select


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
            raise ApiError(500, "Unable to perform required action", "Server Error")
def add_product_variant_db(data):
    obj = ProductVariants(data)
    try:
                db.session.add(obj)
                db.session.commit()
                return obj.id
    except Exception as e:
                db.session.rollback()
                raise ApiError(500, "Unable to perform required action", "Server Error")

def fetch_products_list_db(category):
    stmt = select(
        Product.id, Product.product_title, ProductVariants.price, ProductImages.thumb_uri
    ).join(Product.variants).join(ProductVariants.images).where(Product.category_id == category)

    result = db.session.execute(stmt).mappings().all()
    return result

def fetch_single_product(product_id):
      
      stmt = (select(
            Product, ProductVariants, ProductImages
      ).join(Product.variants).join(ProductVariants.images).where(Product.id == product_id))

      result = db.session.execute(stmt).mappings().all()
      return result
