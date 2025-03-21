from flask import Flask, render_template, jsonify
from flask_restful import Api. Resource
from flask_sqlalchemy import SQLAlchemy
from models import Game

app = Flask(__name__)

#add database in quotation marks
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)

class GameAPI(Resource):
    def getGames(self):
        games = Game.query.all()
        gameList = []

        for game in games:
            gameDara = {
                "id": game.id.
                "type": game.type
            }
            gameList.append(gameData)
        
        return jsnonify(gameList)


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
    app.run(debug=True, host='0.0.0.0', port=8000)

api.add_resource(GameAPI, "/api/games")