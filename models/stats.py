from db import db
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship, backref, joinedload, ColumnProperty, InstrumentedAttribute
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base


class StatsModel(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True, nullable=False)

    fieldGoalsMade = Column(Integer, nullable=False)
    fieldGoalsAttempted = Column(Integer, nullable=False)
    threePointersMade = Column(Integer, nullable=False)
    threePointersAttempted = Column(Integer, nullable=False)
    twoPointersMade = Column(Integer, nullable=False)
    twoPointersAttempted = Column(Integer, nullable=False)
    freeThrowsMade = Column(Integer, nullable=False)
    freeThrowsAttempted = Column(Integer, nullable=False)
    offensiveRebounds = Column(Integer, nullable=False)
    defensiveRebounds = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    steals = Column(Integer, nullable=False)
    blocks = Column(Integer, nullable=False)
    turnovers = Column(Integer, nullable=False)
    personalFouls = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    Poss = Column(Float, nullable=False)
    Plays = Column(Float, nullable=False)
    PPP = Column(Float, nullable=False)
    PPT1 = Column(Float, nullable=False)
    PPT2 = Column(Float, nullable=False)
    PPT3 = Column(Float, nullable=False)
    PPPT1 = Column(Float, nullable=False)
    PPPT2 = Column(Float, nullable=False)
    PPPT3 = Column(Float, nullable=False)
    fieldGoalPercentage = Column(Float, nullable=False)
    threePointPercentage = Column(Float, nullable=False)
    twoPointPercentage = Column(Float, nullable=False)
    freeThrowPercentage = Column(Float, nullable=False)
    player_public_id = Column(String, ForeignKey('players.public_id'), nullable=False)
    game_public_id = Column(String, ForeignKey('games.public_id'), nullable=False)
    team_public_id = Column(String, ForeignKey('teams.public_id'), nullable=False)
    player = relationship("PlayerModel", back_populates="stats")
    game = relationship('GameModel', back_populates="stats")
    team_public_id = Column(Integer, ForeignKey('teams.public_id'))
    # Ensure this matches the relationship name in TeamModel and use 'back_populates'
    team = relationship("TeamModel", back_populates="stats")

    @hybrid_property
    def fieldGoalsMade(self):
        return self.twoPointersMade + self.threePointersMade

    @fieldGoalsMade.expression
    def fieldGoalsMade(cls):
        return cls.twoPointersMade + cls.threePointersMade
    
    @hybrid_property
    def fieldGoalsAttempted(self):
        return self.twoPointersAttempted + self.threePointersAttempted

    @fieldGoalsMade.expression
    def fieldGoalsAttempted(cls):
        return cls.twoPointersAttempted + cls.threePointersAttempted
    
    @hybrid_property
    def points(self):
        return (2 * self.twoPointersMade) + (3 * self.threePointersMade) + self.freeThrowsMade

    @points.expression
    def points(cls):
        return (2 * cls.twoPointersMade) + (3 * cls.threePointersMade) + cls.freeThrowsMade
    
    @hybrid_property
    def Poss(self):
        return self.fieldGoalsAttempted + (0.44 * self.freeThrowsAttempted) + self.turnovers - self.offensiveRebounds

    @hybrid_property
    def Plays(self):
        return self.fieldGoalsAttempted + (0.44 * self.freeThrowsAttempted) + self.turnovers

    @hybrid_property
    def PPP(self):
        return self.points / self.Plays if self.Plays != 0 else 0

    @hybrid_property
    def PPT1(self):
        return self.freeThrowsMade / self.freeThrowsAttempted if self.freeThrowsAttempted != 0 else 0

    @hybrid_property
    def PPT2(self):
        return (self.twoPointersMade * 2) / self.twoPointersAttempted if self.twoPointersAttempted != 0 else 0

    @hybrid_property
    def PPT3(self):
        return (self.threePointersMade * 3) / self.threePointersAttempted if self.threePointersAttempted != 0 else 0

    @hybrid_property
    def PPPT1(self):
        return (self.freeThrowsMade / self.Plays) / self.PPP if self.Plays != 0 and self.PPP != 0 else 0

    @hybrid_property
    def PPPT2(self):
        return ((self.twoPointersMade * 2) / self.Plays) / self.PPP if self.Plays != 0 and self.PPP != 0 else 0

    @hybrid_property
    def PPPT3(self):
        return ((self.threePointersMade * 3) / self.Plays) / self.PPP if self.Plays != 0 and self.PPP != 0 else 0
    
    @hybrid_property
    def fieldGoalPercentage(self):
        return (self.fieldGoalsMade / self.fieldGoalsAttempted * 100) if self.fieldGoalsAttempted else 0

    @hybrid_property
    def threePointPercentage(self):
        return (self.threePointersMade / self.threePointersAttempted * 100) if self.threePointersAttempted else 0

    @hybrid_property
    def twoPointPercentage(self):
        return (self.twoPointersMade / self.twoPointersAttempted * 100) if self.twoPointersAttempted else 0

    @hybrid_property
    def freeThrowPercentage(self):
        return (self.freeThrowsMade / self.freeThrowsAttempted * 100) if self.freeThrowsAttempted else 0
    
    
