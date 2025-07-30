from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    jugadores = relationship("Player", back_populates="equipo")
    zone_teams = relationship("ZoneTeam", back_populates="equipo")
