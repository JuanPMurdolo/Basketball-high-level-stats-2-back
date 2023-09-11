from db import db

class GameVisitorPlayers(db.Model):
    __tablename__ = "game_visitor_players"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    player = db.relationship("Player", backref="game_visitor_players", lazy=True)
    game = db.relationship("Game", backref="game_visitor_players", lazy=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    team = db.relationship("Team", backref="game_visitor_players", lazy=True)
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
    stats = db.relationship("Stats", backref="game_visitor_players", lazy=True)