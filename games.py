from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=false)
    mode = db.Column(db.string(9), nullable=false)

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    request_count = db.Column(db.Integer, default=0)
    rate_limit = db.Column(db.Integer, default=1000)