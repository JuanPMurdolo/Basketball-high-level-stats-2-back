from db import db
from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base

class GameModel(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True, nullable=False)
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    date = Column(DateTime, nullable=False)
    stats_public_id = Column(Integer, ForeignKey('StatsModel.public_id'))
    stats = relationship('StatsModel', back_populates='game')