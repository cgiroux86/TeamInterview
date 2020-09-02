from flask import Blueprint, request, jsonify
from api.models.user_model import User, db
from api.models.teams_model import Team
from flask_jwt import jwt
from api.decorators.decorators import check_for_token
from api.helpers.helpers import current_user
import os
team_bp = Blueprint('team_bp', __name__)


@team_bp.route('/', methods=['POST', 'GET'])
@check_for_token
def create_team():
    user = current_user()
    if request.method == 'POST':
        data = request.get_json(silent=True)
        new_team = Team(user.id, data['name'])
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team.serialize())
    else:
        try:
            teams = Team.query.filter_by(owner_id=user.id).all()
            return jsonify([x.to_dict() for x in teams])

        except Exception as e:
            return jsonify(error=str(e)), 400
