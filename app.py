from flask import Flask
from flask import render_template

app = Flask(__name__)

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