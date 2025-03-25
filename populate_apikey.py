import secrets
from app import app, db
from models import APIKey

api_keys = [
    {"owner": "Frontend App"},
    {"owner": "Admin"},
]

with app.app_context():
    for entry in api_keys:
        new_key = APIKey(
            key=secrets.token_hex(32),
            owner=entry["owner"],
            rate_limit=1000
        )
        db.session.add(new_key)
    
    db.session.commit()
    print("API Keys successfully created and stored in the database.")