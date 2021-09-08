# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
from requests.exceptions import HTTPError
import os, json

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///takerboust.db'
db = SQLAlchemy(app)

"""Landing page route"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addone')
def addone():
    return render_template('addOne.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/org')
def associations():
    return render_template('associations.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/addStudent', methods=['POST', 'GET'])
def create_student():
    universities = get_universities()
    countries = get_countries()
    if request.method == 'POST':
        print("student form send")
    
    return render_template('formulaire.html', countries = countries, universities = universities)

@app.route('/addEmploye', methods=['POST', 'GET'])
def create_employe():
    universities = get_universities()
    countries = get_countries()
    if request.method == 'POST':
        print("employe form send")
    
    return render_template('formulaire.html', countries = countries, universities = universities)

@app.route('/stats')
def stats():
    return "statistics page"


def get_countries():
    try:
        data = []
        response = requests.get('https://restcountries.eu/rest/v2/all')
        json_response = response.json()
        for element in json_response:
            data.append(element["name"])
        return data

    except HTTPError as http_err:
        print(f'Http error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')

def get_universities():
    data = []
    file = open(os.path.join(app.static_folder, "assets/universities.json"), 'r', encoding='utf-8')
    json_file = json.load(file)
    for element in json_file:
        data.append(element["name"])
    return data

if __name__ == "__main__":
    app.run(debug=True)
