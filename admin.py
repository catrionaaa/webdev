from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from models import Game
import requests

app = Flask(__name__)

@app.route('/')
def admin():
    headers = {'X-API-KEY': 'ad18364d5b3f50b20234c13821fe26e5e111a5128c6d3f8d19ed70cdaa4c8add'}
    response = requests.get('http://localhost:8000/api/games', headers=headers)

    if response.status_code == 200:
        table_data = response.json()
    else:
        table_data = [] 

    return render_template('admin.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)