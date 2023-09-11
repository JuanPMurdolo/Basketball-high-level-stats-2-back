from db import db

class Tournament(db.Model):
    __tablename__ = "tournaments"
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    games = db.relationship("Game", backref="tournament", lazy=True)

    def __repr__(self):
        return f"<Tournament {self.name}>"