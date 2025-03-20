from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=false)
    mode = db.Column(db.string(9), nullable=false)