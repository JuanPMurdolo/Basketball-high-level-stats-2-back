from db import db

class TeamStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    stats_id = db.Column(db.Integer, db.ForeignKey("stats.id"))
