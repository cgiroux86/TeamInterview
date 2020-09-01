from flask import Blueprint, request
from api.models.user_model import db
from flask_bcrypt import Bcrypt
from api.models.user_model import User, UserPasswords
import sys
# from flask_jwt import JWT, jwt_required, current_identity
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth/login', methods=["POST"])
def auth():
    data = request.get_json(silent=True)
    # user = User.query.join(UserPasswords, User.id == UserPasswords.user_id).filter(User.email == data['email']).add_columns(
    #     User.id, User.email, UserPasswords.digest).first()
    user = User.query.filter_by(email=data['email']).first()
    print(user.serialize(), flush=True)
    # user.verifyPassword(data['password'])
    return f'{user.verifyPassword(data["password"])}'
