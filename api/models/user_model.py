import sys
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True, nullable=False)
    username = db.Column(db.String(), nullable=True)
    password = db.relationship(
        'UserPasswords', backref=db.backref('users', lazy=True))

    def __init__(self, first_name, last_name, email, username=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username
        }

    def verifyPassword(self, password):
        user_pw = self.password[0].digest
        print('testing', flush=True)
        # return user_pw == received_pw
        return Bcrypt().check_password_hash(user_pw, password)


class UserPasswords(db.Model, SerializerMixin):
    __tablename__ = 'user_passwords'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id'), nullable=False)
    digest = db.Column(db.String(), nullable=False)

    def __init__(self, user_id, digest):
        self.user_id = user_id
        self.digest = Bcrypt().generate_password_hash(digest).decode()

    def __repr__(self):
        return f'user_id: {self.user_id}'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "hash": self.digest
        }
