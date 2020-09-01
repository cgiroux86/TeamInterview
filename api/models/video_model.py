from api.models.user_model import db, User


class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    # owner_id = db.Column(db.Integer(), db.ForeignKey(
    #     'users.id'), nullable=False)
    title = db.Column(db.String(), nullable=False)

    def __init__(self, owner_id, title):
        self.owner_id = owner_id
        self.title = title

    def __repr__(self):
        return f'user_id: {self.owner_id}'
