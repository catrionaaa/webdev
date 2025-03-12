from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/highlow')
def highlow():
    return render_template('highlow.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)