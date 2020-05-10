# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'
app.secret_key = "I prefer nodejs"

db = SQLAlchemy(app)
