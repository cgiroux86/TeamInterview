from flask import request
from flask_jwt import jwt
from api.models.user_model import User
import os


def current_user():
    token = request.headers.get("Authorization")
    token_data = jwt.decode(token, os.environ['SECRET_KEY'])
    user = User.query.get(token_data['user_id'])
    return user
