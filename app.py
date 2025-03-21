from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from games import db, Game

app = Flask(__name__)

#add database in quotation marks
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

class GameAPI(Resource):
    def get(self):
        games = Game.query.all()
        gameList = []

        for game in games:
            gameData = {
                "id": game.id,
                "type": game.type,
            }
            gameList.append(gameData)
        
        return jsonify(gameList)


    def post(self):
        data = request.get_json()

        if not data or "id" not in data or "type" not in data:
            return jsonify({"error": "missing data when recording game"}), 400

        newGame = Game(
            id=data["id"],
            type=data["type"]
        )

        db.session.add(newGame)
        db.session.commit()

        return {"message": "game was successfully recorded"}


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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)

api.add_resource(GameAPI, "/api/games")