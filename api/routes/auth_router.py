from flask import Blueprint, request, jsonify
from api.models.user_model import db
from flask_bcrypt import Bcrypt
from api.models.user_model import User, UserPasswords
import sys
import os
from flask_jwt import jwt
from api.decorators.decorators import check_for_token
import datetime
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=["POST"])
def auth():
    data = request.get_json(silent=True)
    user = User.query.filter_by(email=data['email']).first()
    if user.verifyPassword(data["password"]):

        token = jwt.encode({
            "user": data['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=600),
            "user_id": user.id
        }, os.environ['SECRET_KEY'])

        return jsonify(token=token.decode()), 200
    else:
        return jsonify(message='invalid credentials'), 403


@auth_bp.route('/test_token', methods=["POST"])
@check_for_token
def authorized():
    return 'this means token is working!', 200
