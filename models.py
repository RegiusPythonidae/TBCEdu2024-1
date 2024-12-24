from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db, login_manager


class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()


class Product(db.Model, BaseModel):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    img = db.Column(db.String())
    user_id = db.Column(db.Integer())


class User(db.Model, BaseModel, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    age = db.Column(db.Integer())
    img = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
        self.age = None
        self.img = None

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)