from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.db import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ciudad = Column(String(100))

    # Relationships
    jugadores = relationship("Player", back_populates="equipo")
    zone_teams = relationship("ZoneTeam", back_populates="equipo")
    user_teams = relationship("UserTeam", back_populates="team")
    local_matches = relationship("Match", foreign_keys="Match.local_team_id", back_populates="local_team")
    away_matches = relationship("Match", foreign_keys="Match.away_team_id", back_populates="away_team")
