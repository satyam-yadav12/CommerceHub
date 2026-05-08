from flask import Flask
from config import Config
from .extensions import db
from dotenv import load_dotenv
from .utils.responses.errors import register_error_handler
import cloudinary


def Create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # start extensions by extension.init(app)

    db.init_app(app)

    register_error_handler(app)

    # register important services like cloudinary, google client
    cloudinary.config(
        cloud_name=app.config["CLOUDINARY_CLOUD_NAME"],
        api_key=app.config["CLOUDINARY_API_KEY"],
        api_secret=app.config["CLOUDINARY_API_SECRET"],
        secure=True,
    )

    # register_blueprints
    def register_blueprints():
        from .routes import test_bp

        app.register_blueprint(test_bp, url_prefix="/")

    register_blueprints()
    return app
