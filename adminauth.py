from functools import wraps
from flask import request, jsonify
from models import APIKey


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        from app import app, db
        api_key = request.headers.get('X-API-KEY')

        with app.app_context():
            key_entry = APIKey.query.filter_by(key=api_key).first()

            if not key_entry:
                return {"error": "incorrect api key"}, 403

            key_entry.request_count += 1
            db.session.commit()

        return f(*args, **kwargs)

    return decorated_function