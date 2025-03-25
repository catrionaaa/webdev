import secrets
from app import app, db
from models import APIKey

with app.app_context():
    new_key = APIKey(
        key=secrets.token_hex(32),
        owner="owner"
    )
    db.session.add(new_key)
    
    db.session.commit()
    print("API Key successfully created and stored in the database.")