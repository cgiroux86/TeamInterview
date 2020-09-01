import sys
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True, nullable=False)
    username = db.Column(db.String(), nullable=True)
    password = db.relationship('UserPasswords', backref='user', lazy=True)

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


class UserPasswords(db.Model):
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


# class Video(db.Model):
#     __tablename__ = 'videos'

#     id = db.Column(db.Integer, primary_key=True)
#     owner_id = db.Column(db.Integer(), db.ForeignKey(
#         'users.id'), nullable=False)
#     title = db.Column(db.String(), nullable=False)

#     def __init__(self, owner_id, title):
#         self.owner_id = owner_id
#         self.title = title

#     def __repr__(self):
#         return f'user_id: {self.owner_id}'
