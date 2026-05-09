from flask import request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from ..controllers.admin_controllers import (
    register_admin_controller,
    admin_login_controller,
)

admin = Blueprint("admin", __name__)


@admin.route("/add_admin_data", methods=["POST"])
def register_admin():
    return register_admin_controller()


@admin.route("/login", methods=["POST"])
def admin_login():
    return admin_login_controller()
