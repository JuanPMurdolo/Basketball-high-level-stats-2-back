from db import db

class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    abbreviation = db.Column(db.String(3), nullable=False)
    conference = db.Column(db.String(32), nullable=False)
    division = db.Column(db.String(32), nullable=False)
    court = db.Column(db.String(128), nullable=False)
    alternative_court = db.Column(db.String(128), nullable=True)
    players = db.relationship("Player", backref="team", lazy=True)
    stats = db.relationship("Stats", secondary="team_stats", back_populates="teams", lazy="dynamic")

    def __repr__(self):
        return f"<Team {self.name}>"