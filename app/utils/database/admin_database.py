from ...extensions import db
from sqlalchemy import select
from ..responses.errors import ApiError


def add_admin_data(data):
    try:
        db.session.add(data)
        db.session.commit()
        print(data.id)
        return True
    except Exception as e:
        db.session.rollback()
        return False


def get_user_data(username):
    stmt = select("user").where("user.username" == username)
    result = db.session.execute(stmt).scalar().first()
    if not result:
        raise ApiError(400, "username not Found", "Invalid Data")
    return result
