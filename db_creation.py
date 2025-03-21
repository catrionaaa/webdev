from app import db, app
from games import Game

with app.app_context():
    db.create_all()
    print("Database created")