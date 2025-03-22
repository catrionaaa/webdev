from functools import wraps
from flask import request, jsonify


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')

        if api_key != 'testkey':
            return {"error": "incorrect api key"}, 403

        return f(*args, **kwargs)

    return decorated_function