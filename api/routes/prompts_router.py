from flask import Blueprint, request, jsonify
from api.models.user_model import User, db
from api.models.teams_model import Team
from api.models.prompts_model import Prompt
from flask_jwt import jwt
from api.decorators.decorators import check_for_token
from api.helpers.helpers import current_user
import os
prompt_bp = Blueprint('prompt_bp', __name__)


@prompt_bp.route('/', methods=['POST', 'GET'])
@check_for_token
def create_prompt():
    user = current_user()
    if request.method == 'POST':
        data = request.get_json(silent=True)
        new_prompt = Prompt(
            data['title'], data['question'], user.id, data['team_id'])
        db.session.add(new_prompt)
        db.session.commit()
        return jsonify(new_prompt.to_dict())
    else:
        try:
            user_prompts = Prompt.query.filter_by(owner_id=user.id).all()
            return jsonify([x.to_dict() for x in user_prompts])

        except Exception as e:
            return jsonify(error=str(e)), 400
