from db import db
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

class StatsModel(db.Model):
    __tablename__ = "stats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    field_goal_attempts = db.Column(db.Integer, nullable=False)
    field_goal_made = db.Column(db.Integer, nullable=False)
    
    @hybrid_property
    def field_goal_percentage(self):
        if self.field_goal_attempts == 0:
            return 0.0
        return (self.field_goal_made / self.field_goal_attempts) * 100.0
