from api.models.user_model import db, User
from sqlalchemy_serializer import SerializerMixin


class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'
    serialize_only = ('id', 'name')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    owner_id = db.Column(
        db.Integer(), db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship("User", backref=db.backref('teams', lazy=True))

    def __init__(self, owner_id, name):
        self.owner_id = owner_id
        self.name = name

    def __repr__(self):
        return f'user_id: {self.owner}'

    # def serialize(self):
    #     return {"name": self.name,
    #             "owner_id": self.owner_id}
