from db import db

class PlayerStatsModel(db.Model):
    __tablename__ = "playerstats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"), nullable=False)