from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    type = db.Column(db.String(9), nullable=False)

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    request_count = db.Column(db.Integer, default=0)
    rate_limit = db.Column(db.Integer, default=1000)