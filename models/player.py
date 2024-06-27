from db import db
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base

class PlayerModel(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True, nullable=False)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    stats = relationship("StatsModel", back_populates="player")
    team_public_id = Column(String, ForeignKey('teams.public_id'), nullable=False)
    team = relationship("TeamModel", back_populates="players")