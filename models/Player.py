from db import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(80), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    stats = db.relationship('Stat', backref='player', lazy=True)

    def __repr__(self):
        return f'<Player {self.name}>'