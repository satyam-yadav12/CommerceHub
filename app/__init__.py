from flask import Flask
from .config import Config
from .extensions import db
from dotenv import load_dotenv
from .responses.errors import register_error_handler


def Create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # start extensions by extension.init(app)

    db.init_app(app)

    register_error_handler(app)

    # register important services like cloudinary, google client
    # register_blueprints
    def register_blueprints():
        from .routes.auth_routes import auth_bp

        app.register_blueprint(auth_bp, url_prefix="/")

    register_blueprints()
    return app
