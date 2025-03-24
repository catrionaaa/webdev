from app import db, app
from models import Game

with app.app_context():
    db.create_all()
    print("Database created")