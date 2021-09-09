# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from jinja2.loaders import PrefixLoader
import requests
from requests.exceptions import HTTPError
import os, json
from datetime import datetime

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///takerboust.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""Database models"""
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.DateTime, nullable=False)
    sexe = db.Column(db.String(10), nullable=False)
    pays = db.Column(db.String(30), nullable=False)
    niveau_etude = db.Column(db.String(10), nullable=False)
    universite = db.Column(db.String(100), nullable=False)
    specialite = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return "Student %r" % self.id

class Employe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.DateTime, nullable=False)
    sexe = db.Column(db.String(10), nullable=False)
    pays = db.Column(db.String(30), nullable=False)
    fonction = db.Column(db.String(30), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return "Employe %r" % self.id



"""Routes"""
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
        y, m, d = request.form.get('date_naissance').split('-')
        birthday = datetime(int(y), int(m), int(d))
        student = Student(
            nom = request.form.get("nom"),
            prenom = request.form.get("prenom"),
            date_naissance = birthday,
            sexe = request.form.get("sexe"),
            pays = request.form.get("pays"),
            universite = request.form.get("universite"),
            niveau_etude = request.form.get("niveau_etude"),
            specialite = request.form.get("specialite")
        )
        db.session.add(student)
        db.session.commit()
    
    return render_template('formulaire.html', countries = countries, universities = universities)

@app.route('/addEmploye', methods=['POST', 'GET'])
def create_employe():
    universities = get_universities()
    countries = get_countries()
    if request.method == 'POST':
        y, m, d = request.form.get('date_naissance').split('-')
        birthday = datetime(int(y), int(m), int(d))
        employe = Employe(
            nom = request.form.get("nom"),
            prenom = request.form.get("prenom"),
            date_naissance = birthday,
            sexe = request.form.get("sexe"),
            pays = request.form.get("pays"),
            fonction = request.form.get("fonction"),
            experience = request.form.get("experience")
        )
        db.session.add(employe)
        db.session.commit()
    
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
