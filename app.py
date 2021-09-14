# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
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
    formation = db.Column(db.String(50), nullable=False)
    obtention = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return "Student %r" % self.id

class Employe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.DateTime, nullable=False)
    sexe = db.Column(db.String(10), nullable=False)
    diplome = db.Column(db.String(10), nullable=False)
    pays = db.Column(db.String(30), nullable=False)
    fonction = db.Column(db.String(30), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return "Employe %r" % self.id



"""Routes"""
@app.route('/')
def index():
    return render_template('index.html')


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
    formations = get_formations("all")
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
            formation = request.form.get("specialite"),
            niveau_etude = request.form.get("niveau_etude"),
            obtention = request.form.get("obtention")
        )
        db.session.add(student)
        db.session.commit()
    
    return render_template('formulaire.html', countries = countries, universities = universities, formations = formations)

@app.route('/addEmploye', methods=['POST', 'GET'])
def create_employe():
    universities = get_universities()
    countries = get_countries()
    formations = get_formations("all")
    if request.method == 'POST':
        y, m, d = request.form.get('date_naissance').split('-')
        birthday = datetime(int(y), int(m), int(d))
        employe = Employe(
            nom = request.form.get("nom"),
            prenom = request.form.get("prenom"),
            date_naissance = birthday,
            sexe = request.form.get("sexe"),
            pays = request.form.get("pays"),
            diplome = request.form.get("diplome"),
            fonction = request.form.get("fonction"),
            experience = request.form.get("experience")
        )
        db.session.add(employe)
        db.session.commit()
    
    return render_template('formulaire.html', countries = countries, universities = universities, formations = formations)

@app.route('/stats')
def stats():
    return "statistics page"

"""Api endpoints"""
@app.route('/api/get-formations-by-degree', methods=['POST', 'GET'])
def get_formations_by_degree():
    names = {"l1": "Licence 1", "l2": "Licence 2", "l3": "Licence 3", "m1": "Master 1", "m2": "Master 2"}
    if request.method == "POST":
        degree = json.loads(request.data)['degree']
        all_data = get_formations(names[degree])
        return json.dumps(all_data)
    
    return None

@app.route('/api/students-by-degree', methods=['GET'])
def students_by_degree():
    if request.method == "GET":
        data = db.session.query(Student.niveau_etude, func.count(Student.id)).group_by(Student.niveau_etude).all()
        print(data)
    return "hello"



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

def get_formations(degree : str):
    data = []
    file = open(os.path.join(app.static_folder, "assets/formations.json"), 'r', encoding='utf-8')
    json_file = json.load(file)

    if degree == "all":
        for element in json_file:
            data.append(element["formation"])
        return data
    
    for element in json_file:
        if element["degree"] == degree:
            data.append(element["formation"])
    return data


def get_universities():
    data = []
    file = open(os.path.join(app.static_folder, "assets/universities.json"), 'r', encoding='utf-8')
    json_file = json.load(file)
    for element in json_file:
        data.append(element["name"])
    return data



if __name__ == "__main__":
    app.run(debug=True)