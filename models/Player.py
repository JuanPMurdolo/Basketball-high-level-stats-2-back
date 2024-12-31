from db import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(80), nullable=True)
    first_division = db.Column(db.Boolean, nullable=True)
    years_active = db.Column(db.Integer, nullable=True)
    teams = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<Player {self.name}>'