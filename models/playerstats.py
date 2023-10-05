from db import db

class PlayerStats(db.Model):
    __tablename__ = "player_stats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
    