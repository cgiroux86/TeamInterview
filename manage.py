from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from app import application
from api.models.user_model import db

migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
