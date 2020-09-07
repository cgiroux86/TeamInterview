from flask import Blueprint, request, jsonify
from api.models.user_model import User, db
from api.models.teams_model import Team
from api.models.prompts_model import Prompt
from flask_jwt import jwt
from api.decorators.decorators import check_for_token
from api.helpers.helpers import current_user
from functools import wraps
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
        return jsonify(new_team.to_dict())
    else:
        try:
            teams = Team.query.filter_by(owner_id=user.id).all()
            return jsonify([x.to_dict() for x in teams])

        except Exception as e:
            return jsonify(error=str(e)), 400


@team_bp.route('/<team_id>/prompts', methods=["GET"])
@check_for_token
def get_team_prompts(team_id):
    team_id = team_id
    try:

        prompts = Prompt.query.filter_by(team_id=team_id).all()
        return jsonify([prompt.to_dict() for prompt in prompts])
    except Exception as e:
        return jsonify(error=str(e)), 400
