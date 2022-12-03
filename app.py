from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '3b6dbc5e2b88694100ea481536b72ff2'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    gebruikersnaam = db.Column(db.String(20), nullable=False)
    wachtwoord = db.Column(db.String(80), nullable=False)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/registreer")
def registreer():
    return render_template('registreer.html')
