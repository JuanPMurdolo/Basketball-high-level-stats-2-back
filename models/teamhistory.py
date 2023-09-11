from db import db

class TeamHistory(db.Model):
    __tablename__ = "team_history"
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(32), db.ForeignKey('players.id'), nullable=False)
    team_id = db.Column(db.Integer)
    actual_team = db.Column(db.Boolean)
    beggining_of_contract = db.Column(db.Date)
    end_of_contract = db.Column(db.Date)