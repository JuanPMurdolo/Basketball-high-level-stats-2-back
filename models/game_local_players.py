from db import db

class GameLocalPlayers(db.Model):
    __tablename__ = "game_local_players"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    player = db.relationship("Player", backref="game_local_players", lazy=True)
    game = db.relationship("Game", backref="game_local_players", lazy=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team = db.relationship("Team", backref="game_local_players", lazy=True)
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
    stats = db.relationship("Stats", backref="game_local_players", lazy=True)