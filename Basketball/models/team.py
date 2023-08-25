from db import db

class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    players = db.relationship("Player", backref="team", lazy=True)

    def __repr__(self):
        return f"<Team {self.name}>"