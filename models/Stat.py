from db import db

class Stat(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, nullable=False)
    rebounds_def = db.Column(db.Integer, nullable=False)
    rebounds_off = db.Column(db.Integer, nullable=False)
    rebounds_total = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    steals = db.Column(db.Integer, nullable=False)
    blocks = db.Column(db.Integer, nullable=False)
    field_goal_attempts = db.Column(db.Integer, nullable=False)
    field_goal_makes = db.Column(db.Integer, nullable=False)
    free_throw_attempts = db.Column(db.Integer, nullable=False)
    free_throw_makes = db.Column(db.Integer, nullable=False)
    three_point_attempts = db.Column(db.Integer, nullable=False)
    three_point_makes = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

    def __repr__(self):
        return f'<Stat {self.id}>'