from db import db

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable = True)
    date_of_birth = db.Column(db.String(64), nullable=True)
    picture = db.Column(db.String(64), nullable=True)
    position = db.Column(db.String(64), nullable=True)
    historical_team_id = db.Column(db.String(64), nullable=True)
    games = db.Column(db.Integer, nullable=True)
    games_started = db.Column(db.Integer, nullable=True)
    # Agrega una clave foránea que haga referencia a Team
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    # Agrega una relación con Stats
    stats = db.relationship("Stats", secondary="player_stats", back_populates="players", lazy="dynamic", single_parent=True)
    def __repr__(self):
        return f"<Player {self.name}>"