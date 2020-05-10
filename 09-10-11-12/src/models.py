from app import db

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


class Contact(db.Model):
    """"""
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    birthday = db.Column(db.String)
    email = db.Column(db.String)
    profession = db.Column(db.String)
    interests = db.Column(db.String)
    phone_number = db.Column(db.String)


class User(UserMixin, db.Model):
    """"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
