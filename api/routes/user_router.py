from flask import Blueprint, request
from app import *
from api.models.user_model import User
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/test', methods=['GET'])
def test():
    return 'it works!'


@user_bp.route('/register', methods=['POST'])
def register():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    password = request.args.get('password')

    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return "User added. book id={}".format(user.id)
    except Exception as e:
        return(str(e))
