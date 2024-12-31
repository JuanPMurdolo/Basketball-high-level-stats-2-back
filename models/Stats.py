from db import db

class Stats(db.Model):
    __tablename__ = 'stats'

    points = db.Column(db.Integer, nullable=True)
    rebounds = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    steals = db.Column(db.Integer, nullable=True)
    blocks = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    fouls = db.Column(db.Integer, nullable=True)
    minutes = db.Column(db.Integer, nullable=True)
    field_goals_made = db.Column(db.Integer, nullable=True)
    field_goals_attempted = db.Column(db.Integer, nullable=True)
    two_points_made = db.Column(db.Integer, nullable=True)
    two_points_attempted = db.Column(db.Integer, nullable=True)
    three_points_made = db.Column(db.Integer, nullable=True)
    three_points_attempted = db.Column(db.Integer, nullable=True)
    free_throws_made = db.Column(db.Integer, nullable=True)
    free_throws_attempted = db.Column(db.Integer, nullable=True)

    
    def __repr__(self):
        return f'<Stats {self.id}>'