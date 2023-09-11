from db import db

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(64), nullable = True)
    date_of_birth = db.Column(db.String(64), nullable=True)
    picture = db.Column(db.String(64), nullable=True)
    position = db.Column(db.String(64), nullable=True)
    historical_team_id = db.Column(db.String(64), nullable=True)
    games = db.Column(db.Integer, nullable=True)
    games_started = db.Column(db.Integer, nullable=True)
    minutes_played = db.Column(db.Integer, nullable=True)
    historical_teams = db.relationship('TeamHistory', backref='player', lazy=True)
    def __repr__(self):
        return f"<Player {self.name}>"