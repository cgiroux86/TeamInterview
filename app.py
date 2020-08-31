import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import user_router
application = Flask(__name__)
application.register_blueprint(user_router.test_bp)
application.config.from_object(os.environ['APP_SETTINGS'])
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
from models.user_model import User
db.init_app(application)


@application.route('/', methods=["GET"])
def hello():
    return 'Hello World'


# @app.route('/test', methods=[])
if __name__ == '__main__':
    port = os.getenv('PORT', default='5000')
    application.run('0.0.0.0', port=port)
