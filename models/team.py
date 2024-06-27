from db import db
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base
from .stats import StatsModel
from .game import GameModel
from .player import PlayerModel

class TeamModel(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    public_id = Column(String, unique=True, nullable=False)

    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)

    players = relationship("PlayerModel", back_populates="team")
    stats = relationship("StatsModel", back_populates="team")