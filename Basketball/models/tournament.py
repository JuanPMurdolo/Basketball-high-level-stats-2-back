from db import db

class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.String(32), primary_key=True)
    date = db.Column(db.Date, nullable=False)
    local_team_id = db.Column(db.String(32), db.ForeignKey("teams.id"), nullable=False)
    visitor_team_id = db.Column(db.String(32), db.ForeignKey("teams.id"), nullable=False)
    local_team = db.relationship("Team", foreign_keys=[local_team_id])
    visitor_team = db.relationship("Team", foreign_keys=[visitor_team_id])
    local_score = db.Column(db.Integer, nullable=False)
    visitor_score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    season = db.Column(db.String(32), nullable=False)
    season_type = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    post_season = db.Column(db.Boolean, nullable=False)
    home_team_wins = db.Column(db.Boolean, nullable=False)
    home_team_losses = db.Column(db.Boolean, nullable=False)
    visitor_team_wins = db.Column(db.Boolean, nullable=False)
    visitor_team_losses = db.Column(db.Boolean, nullable=False)
    local_team_stats = db.Column(db.JSON, nullable=False)
    visitor_team_stats = db.Column(db.JSON, nullable=False)