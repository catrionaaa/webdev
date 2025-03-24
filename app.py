app = Flask(__name__)
from flask import Flask, render_template, jsonify, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from games import db, Game, GameAPI
from deckOfCards import DeckOfCardsAPI
from flasgger import Swagger
swagger = Swagger(app)
db.init_app(app)
api = Api(app)

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
api.add_resource(GameAPI, "/api/games", endpoint="games")

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

@app.route('/admin')
def admin():
    return render_template('admin.html')

# --------------------------
# Deck of Cards API Routes
# --------------------------

# Create a new shuffled deck
@app.route('/api/deck/new', methods=['GET'])
def new_deck():
    deck_data = DeckOfCardsAPI.new_deck()
    return jsonify(deck_data)

# Draw cards from a specific deck
@app.route('/api/deck/<deck_id>/draw', methods=['GET'])
def draw_cards(deck_id):
    count = request.args.get('count', default=1, type=int)
    cards_data = DeckOfCardsAPI.draw_cards(deck_id, count)
    return jsonify(cards_data)

# Shuffle an existing deck
@app.route('/api/deck/<deck_id>/shuffle', methods=['GET'])
def shuffle_deck(deck_id):
    shuffle_data = DeckOfCardsAPI.shuffle_deck(deck_id)
    return jsonify(shuffle_data)

# --------------------------
# Run the app
# --------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

@app.route('/api/deck/new', methods=['GET'])
def new_deck():
    """
    Create a new shuffled deck
    ---
    responses:
      200:
        description: A new shuffled deck was created
    """
    deck_data = DeckOfCardsAPI.new_deck()
    return jsonify(deck_data)
