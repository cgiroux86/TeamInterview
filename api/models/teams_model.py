from api.models.user_model import db, User


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    # owner_id = db.Column(db.Integer(), db.ForeignKey(
    #     'users.id'), nullable=False)
    name = db.Column(db.String(), nullable=False)
    owner_id = db.Column(
        db.Integer(), db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", backref=db.backref('teams', lazy=True))

    def __init__(self, owner_id, name):
        self.owner = owner_id
        self.name = name

    def __repr__(self):
        return f'user_id: {self.owner}'
