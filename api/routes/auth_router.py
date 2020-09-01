from flask import Blueprint, request
from api.models.user_model import db
from flask_bcrypt import Bcrypt
from api.models.user_model import User, UserPasswords
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth/login', methods=["POST"])
def auth():
    data = request.get_json(silent=True)
    user = User.query.join(UserPasswords, User.id == UserPasswords.user_id).filter(User.email == data['email']).add_columns(
        User.id, User.email, UserPasswords.digest).first()
    return f'{user[3]}'
