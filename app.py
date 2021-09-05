from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///takerboust.db'
db = SQLAlchemy(app)

"""Landing page route"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addOne')
def inscription():
    return render_template('formulaire.html')

@app.route('/addStudent', methods=['POST', 'GET'])
def create_student():
    if request.method == 'POST':
        pass

    return render_template('formulaire.html')

@app.route('/stats')
def stats():
    return "statistics page"

if __name__ == "__main__":
    app.run(debug=True)
