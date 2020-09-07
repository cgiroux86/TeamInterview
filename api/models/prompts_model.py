from api.models.user_model import db, User
from sqlalchemy_serializer import SerializerMixin


class Prompt(db.Model, SerializerMixin):
    __tablename__ = 'prompts'
    serialize_only = ("id", "title", "question")

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    question = db.Column(db.String(), nullable=False)
    owner_id = db.Column(
        db.Integer(), db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", backref=db.backref('prompts', lazy=True))
    team_id = db.Column(db.Integer(), db.ForeignKey(
        "teams.id"), nullable=False)
    team = db.relationship('Team', backref=db.backref('prompts', lazy=True))

    def __init__(self, title, question, owner_id, team_id):
        self.owner_id = owner_id
        self.title = title
        self.question = question
        self.team_id = team_id

    def __repr__(self):
        return f'user_id: {self.owner_id}'

    # def serialize(self):
    #     return {"name": self.name,
    #             "owner_id": self.owner_id}
