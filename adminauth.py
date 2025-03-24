#from functools import wraps
#from flask import request

from flask import request, jsonify
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for an admin key in the request headers
        admin_key = request.headers.get('Admin-Key')
        if admin_key != "your_secret_admin_key":  # Replace with a secure key
            return jsonify({"message": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function