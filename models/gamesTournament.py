from db import db

class GamesTournament(db.Model):
    __tablename__ = "games_tournament"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id"))