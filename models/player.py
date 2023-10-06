from db import db

class PlayerModel(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    stats = db.relationship("StatsModel", backref="player", lazy=True)


