from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from models import db, Game, GameAPI
from deckOfCards import DeckOfCardsAPI
from flasgger import Swagger
from adminauth import require_api_key, require_api_key_admin

# --------------------------
# Initialize Flask app
# --------------------------
app = Flask(__name__)

# --------------------------
# Configure SQLite database
# --------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --------------------------
# Initialize and create DB
# --------------------------
db.init_app(app)
with app.app_context():
    db.create_all()

# --------------------------
# Initialize Flask-RESTful API
# --------------------------
api = Api(app)
#api.add_resource(GameAPI, "/api/games", endpoint="games")

# --------------------------
# Page Routes
# --------------------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/snap')
def snap():
    return render_template("snap.html")

@app.route('/selectgame')
def selectgame():
    return render_template("selectgame.html")

@app.route('/settings')
def settings():
    return render_template('settings.html')

# --------------------------
# Deck of Cards API Routes
# --------------------------
'''
# Create a new shuffled deck
@app.route('/api/deck/new', methods=['GET'])
def new_deck():
    """
    Create a new shuffled deck
    ---
    tags:
      - Deck of Cards
    responses:
      200:
        description: A new shuffled deck was created
        content:
          application/json:
            schema:
              type: object
              properties:
                success:
                  type: boolean
                deck_id:
                  type: string
                remaining:
                  type: integer
    """
    deck_data = DeckOfCardsAPI.new_deck()
    return jsonify(deck_data)

# Draw cards from a specific deck
@app.route('/api/deck/<deck_id>/draw', methods=['GET'])
def draw_cards(deck_id):
    """
    Draw cards from a specific deck
    ---
    tags:
      - Deck of Cards
    parameters:
      - name: deck_id
        in: path
        required: true
        description: The ID of the deck
        schema:
          type: string
      - name: count
        in: query
        required: false
        description: Number of cards to draw (default is 1)
        schema:
          type: integer
    responses:
      200:
        description: Cards drawn from the deck
        content:
          application/json:
            schema:
              type: object
              properties:
                success:
                  type: boolean
                cards:
                  type: array
                  items:
                    type: object
    """
    count = request.args.get('count', default=1, type=int)
    cards_data = DeckOfCardsAPI.draw_cards(deck_id, count)
    return jsonify(cards_data)

# Shuffle an existing deck
@app.route('/api/deck/<deck_id>/shuffle', methods=['GET'])
def shuffle_deck(deck_id):
    """
    Shuffle an existing deck
    ---
    tags:
      - Deck of Cards
    parameters:
      - name: deck_id
        in: path
        required: true
        description: The ID of the deck
        schema:
          type: string
    responses:
      200:
        description: The deck was shuffled
        content:
          application/json:
            schema:
              type: object
              properties:
                success:
                  type: boolean
    """
    shuffle_data = DeckOfCardsAPI.shuffle_deck(deck_id)
    return jsonify(shuffle_data)
'''
# --------------------------
# Flask endpoints
# --------------------------

class GameAPI(Resource):
    @require_api_key_admin
    def get(self):
        """
        Get all games
        ---
        tags:
          - Games
        responses:
          200:
            description: A list of all games
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                      mode:
                        type: string
        """
        games = Game.query.all()
        gameList = [{"id": game.id, "mode": game.mode} for game in games]
        return jsonify(gameList)

    @require_api_key
    def post(self):
        """
        Add a new game
        ---
        tags:
          - Games
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  mode:
                    type: string
        responses:
          201:
            description: Game successfully added
        """
        data = request.get_json()

        if not data.get("mode"):
            return {"error": "Missing required field 'mode'"}
        
        newGame = Game(mode=data["mode"])
        db.session.add(newGame)
        db.session.commit()

        return {"message": "Game successfully added"}, 201

    @require_api_key_admin
    def put(self):
        """
        Update an existing game
        ---
        tags:
          - Games
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                  mode:
                    type: string
        responses:
          200:
            description: Game successfully updated
        """
        data = request.json
        gameId = data.get("id")

        game = Game.query.get(gameId)
        if not game:
            return {"error": "could not find game ID"}
        
        game.mode = data["mode"]
        db.session.commit()

        return {"message": "game successfully updated"}

    @require_api_key_admin
    def delete(self):
        """
        Delete a game
        ---
        tags:
          - Games
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
        responses:
          200:
            description: Game successfully deleted
        """
        data = request.json
        gameId = data.get("id")

        game = Game.query.get(gameId)
        if not game:
            return {"error": "could not find game ID"}
        
        db.session.delete(game)
        db.session.commit()

        return {"message": "game successfully deleted"}

api.add_resource(GameAPI, "/api/games", endpoint="games")

# --------------------------
# Run the app
# --------------------------

swagger = Swagger(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)