from db import db

class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.String(32), primary_key=True)
    date = db.Column(db.String(32))
    local_team_id = db.Column(db.String(32), db.ForeignKey("teams.id"), nullable=False)
    visitor_team_id = db.Column(db.String(32), db.ForeignKey("teams.id"), nullable=False)
    #local_team = db.relationship("Team", foreign_keys=[local_team_id])
    #visitor_team = db.relationship("Team", foreign_keys=[visitor_team_id])
    #local_score = db.Column(db.Integer)
    #visitor_score = db.Column(db.Integer)
    #season = db.Column(db.String(32))
    #season_type = db.Column(db.String(32))
    #status = db.Column(db.String(32))
    #post_season = db.Column(db.Boolean)
    #home_team_wins = db.Column(db.Boolean)
    #referees = db.Column(db.String(128))
    #court = db.Column(db.String(128))
    tournament = db.relationship("Tournament", secondary="games_tournament", back_populates='games', lazy="dynamic", single_parent=True)

    
