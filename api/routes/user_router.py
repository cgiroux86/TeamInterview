from flask import Blueprint, request
from api.models.user_model import User, db
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

    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        db.session.add(user)
        db.session.commit()
        return "User added. book id={}".format(user.id)
    except Exception as e:
        return(str(e))
