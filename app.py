from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
from requests.exceptions import HTTPError

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

@app.route('/addStudent', methods=['POST', 'GET'])
def create_student():
    countries = getCountries()
    if request.method == 'POST':
        print("student form send")
    
    return render_template('formulaire.html', countries = countries)

@app.route('/addEmploye', methods=['POST', 'GET'])
def create_employe():
    countries = getCountries()
    if request.method == 'POST':
        print("employe form send")
    
    return render_template('formulaire.html', countries = countries)

@app.route('/stats')
def stats():
    return "statistics page"


def getCountries():
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


if __name__ == "__main__":
    app.run(debug=True)
