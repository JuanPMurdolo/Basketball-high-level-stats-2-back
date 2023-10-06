from db import db
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

class StatsModel(db.Model):
    __tablename__ = "stats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    #Two point
    two_point_attempts = Column(Integer, nullable=False, default=0)
    two_point_made = Column(Integer, nullable=False, default=0)
    #Three point
    three_point_attempts = Column(Integer, nullable=False, default=0)
    three_point_made = Column(Integer, nullable=False, default=0)
    
    @hybrid_property
    def field_goal_attempts(self):
        return self.two_point_attempts + self.three_point_attempts

    @hybrid_property
    def field_goal_made(self):
        return self.two_point_made + self.three_point_made
    
    @hybrid_property
    def two_point_percentage(self):
        if self.two_point_attempts == 0:
            return 0.0
        return (self.two_point_made / self.two_point_attempts) * 100.0
    
    @hybrid_property
    def three_point_percentage(self):
        if self.three_point_attempts == 0:
            return 0.0
        return (self.three_point_made / self.three_point_attempts) * 100.0

    @hybrid_property
    def field_goal_percentage(self):
        if self.field_goal_attempts == 0:
            return 0.0
        return (self.field_goal_made / self.field_goal_attempts) * 100.0
