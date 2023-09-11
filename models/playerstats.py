from db import db

class PlayerStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
    