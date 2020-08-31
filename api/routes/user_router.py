from flask import Blueprint, request
from api.models.user_model import User, UserPasswords, db
from flask_bcrypt import Bcrypt
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/test', methods=['GET'])
def test():
    return 'it works!'


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    digest = data['password']

    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return(str(e))

    try:
        user_pw = UserPasswords(
            user_id=user.id,
            digest=digest
        )
        db.session.add(user_pw)
        db.session.commit()
        return f'User with id of {user.id}, has successfully saved password {user_pw.digest}'
    except Exception as e:
        return str(e)
