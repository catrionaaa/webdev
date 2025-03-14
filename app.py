from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/highlow')
def highlow():
    return render_template('highlow.html')

@app.route('/twentyone')
def twentyone():
    return render_template("twentyone.html")

@app.route('/pairs')
def pairs():
    return render_template("pairs.html")

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)