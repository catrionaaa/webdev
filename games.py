from flask_restful import Resource, reqparse
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from adminauth import admin_required  # Import your admin check decorator

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

    # GET: Retrieve all games
    def get(self):
        games = Game.query.all()
        game_list = [{"id": game.id, "mode": game.mode} for game in games]
        return jsonify(game_list)

    # POST: Add a new game (Admin only)
    @admin_required
    def post(self):
        args = self.parser.parse_args()
        new_game = Game(mode=args['mode'])
        db.session.add(new_game)
        db.session.commit()
        return jsonify({"message": "Game created", "id": new_game.id})

    # PUT: Update a game by ID (Admin only)
    @admin_required
    def put(self, game_id):
        args = self.parser.parse_args()
        game = Game.query.get(game_id)
        if game:
            game.mode = args['mode']
            db.session.commit()
            return jsonify({"message": "Game updated", "id": game.id})
        return jsonify({"message": "Game not found"}), 404

    # DELETE: Remove a game by ID (Admin only)
    @admin_required
    def delete(self, game_id):
        game = Game.query.get(game_id)
        if game:
            db.session.delete(game)
            db.session.commit()
            return jsonify({"message": "Game deleted", "id": game.id})
        return jsonify({"message": "Game not found"}), 404
