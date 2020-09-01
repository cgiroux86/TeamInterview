from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from api.routes import user_router, auth_router
from api.models.user_model import User, UserPasswords, db
from api.models.video_model import Video


def create_app():
    application = Flask(__name__)
    application.register_blueprint(user_router.user_bp)
    application.register_blueprint(auth_router.auth_bp)
    application.config.from_object(os.environ['APP_SETTINGS'])
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(application)
    return application


application = create_app()
if __name__ == '__main__':
    port = os.getenv('PORT', default='5000')
    application.run('0.0.0.0', port=port)
