from flask import Blueprint, request, jsonify
from api.models.user_model import db
from flask_bcrypt import Bcrypt
from api.models.user_model import User, UserPasswords
import sys
import os
from flask_jwt import jwt
import datetime
auth_bp = Blueprint('auth_bp', __name__)

"""decorator function to validate JWT"""


def check_for_token(func):
    def wrapped():
        token = request.headers.get('Authorization')
        if not token:
            return jsonify(error='unauthorized'), 401
        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'])
        except:
            return jsonify(error='unauthorized'), 401
        return func()
    return wrapped


@auth_bp.route('/auth/login', methods=["POST"])
def auth():
    data = request.get_json(silent=True)
    user = User.query.filter_by(email=data['email']).first()
    if user.verifyPassword(data["password"]):
        token = jwt.encode({
            "user": data['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        }, os.environ['SECRET_KEY'])
        return jsonify(token=token.decode()), 200


@auth_bp.route('/auth/test_token', methods=["POST"])
@check_for_token
def authorized():
    return 'this means token is working!', 200
