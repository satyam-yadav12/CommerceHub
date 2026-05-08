from flask import jsonify


def create_success_response(status, message, data=None):

    return jsonify({"success": True, "message": message, "data": data}), status
