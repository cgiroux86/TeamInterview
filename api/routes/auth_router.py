from flask import Blueprint, request
from api.models.user_model import db
from flask_bcrypt import Bcrypt
from api.models.user_model import User
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth/login')
def auth():
    # data = request.get_json(silent=True)
    # user = User.query.filter_by(email=data['email']).first()
    # user_pw = user.userpassword
    pass
