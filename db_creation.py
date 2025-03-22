from app import db, app
from models import APIKey

with app.app_context():
    db.create_all()
    print("Database created")