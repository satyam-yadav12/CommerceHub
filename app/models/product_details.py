from ..extensions import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_title = db.Column(db.String(100), nullable=False)
    product_description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("product_categories.id"))
    variants = db.relationship("ProductVariants", backref="product", lazy=True)


class ProductCategories(db.Model):
    __tablename__ = "product_categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(20), nullable=False)
    products = db.relationship("Product", backref="category", lazy=True)


class ProductVariants(db.Model):
    __tablename__ = "product_variants"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    variant_name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(20), nullable=True)
    size = db.Column(db.String(20), nullable=True)
    weight = db.Column(db.String(20), nullable=True)
    images = db.relationship("ProductImages", backref="product_variants", lazy=True)
    orders = db.relationship("OrderItems", backref="product", lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Numeric(10, 2), nullable=False)


class ProductImages(db.Model):
    __tablename__ = "product_images"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_title = db.Column(db.String(100), nullable=False)
    image_width = db.Column(db.Float, nullable=False)
    image_height = db.Column(db.Float, nullable=False)
    image_uri = db.Column(db.String(500), nullable=False)
    thumb_uri = db.Column(db.String(500), nullable=False)
    product_variant = db.Column(
        db.Integer, db.ForeignKey("product_variants.id"), nullable=False
    )
