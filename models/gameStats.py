from db import db

class GameStats(db.Model):
    __tablename__ = "games_stats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
