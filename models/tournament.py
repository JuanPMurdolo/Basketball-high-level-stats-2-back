from db import db

class Tournament(db.Model):
    __tablename__ = "tournaments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=True)
    season = db.Column(db.String(32), nullable=True)
    season_type = db.Column(db.String(32), nullable=True)
    start_date = db.Column(db.String(32), nullable=True)
    end_date = db.Column(db.String(32), nullable=True)
    games = db.relationship("Game", secondary="games_tournament", back_populates='tournament', lazy="dynamic", cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return f"<Tournament {self.name}>"