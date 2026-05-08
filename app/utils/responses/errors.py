from flask import jsonify
from werkzeug.exceptions import HTTPException


class ApiError(Exception):
    def __init__(self, status, message, error_type):
        super().__init__(message)
        self.status_code = status
        self.error_type = error_type


def register_error_handler(app):
    @app.errorhandler(ApiError)
    def handleCustomError(e):
        return (
            jsonify(
                {"success": False, "error": {"type": e.error_type, "message": str(e)}}
            ),
            e.status_code,
        )

    @app.errorhandler(HTTPException)
    def handleHttpError(e):
        return (
            jsonify(
                {
                    "success": False,
                    "error": {
                        "type": "HTTP Error",
                        "message": e.description,
                    },
                }
            ),
            e.code,
        )

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        return (
            jsonify(
                {
                    "success": False,
                    "error": {
                        "type": "Server Error",
                        "message": "Interner Server Error",
                    },
                }
            ),
            500,
        )
