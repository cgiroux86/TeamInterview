from flask import Blueprint, request, jsonify
from api.models.user_model import User, UserPasswords, db
from flask_bcrypt import Bcrypt
user_bp = Blueprint('user_bp', __name__)


def validate_register_fields(req):
    data = req.get_json(silent=True)
    fields = ['first_name', 'last_name', 'email', 'password']
    for f in fields:
        if f not in data:
            return False
    return True


@user_bp.route('/test', methods=['POST'])
def test():
    return f'{validate_register_fields(request)}'


@user_bp.route('/register', methods=['POST'])
def register():
    if validate_register_fields(request):
        data = request.get_json(silent=True)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        digest = data['password']

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        try:
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

            return jsonify(user.serialize()), 201
        except Exception as e:
            return str(e)
    else:
        return jsonify(error='missing required fields with a hot reload!'), 400
