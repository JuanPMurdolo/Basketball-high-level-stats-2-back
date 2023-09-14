from db import db

class GameStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
