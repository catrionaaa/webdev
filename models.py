from flask_restful import Resource, reqparse
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

# --------------------------
# Initialize the database
# --------------------------
db = SQLAlchemy()

# --------------------------
# Game Model (SQLAlchemy)
# --------------------------
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(100), nullable=False)  # Game mode: e.g., 'Snap', 'Blackjack'

# --------------------------
# RESTful API Resource
# --------------------------
class GameAPI(Resource):
    # Parser to validate and extract 'mode' from request body
    parser = reqparse.RequestParser()
    parser.add_argument('mode', type=str, required=True, help='Game mode is required')

# --------------------------
# Admin key model
# --------------------------
class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    request_count = db.Column(db.Integer, default=0)
    rate_limit = db.Column(db.Integer, default=1000)
