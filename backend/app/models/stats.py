from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base

class BasketballStats(Base):
    __tablename__ = "basketball_stats"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"))
    jugador_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"))
    team_id = Column(Integer, ForeignKey("teams.id"))

    minutos = Column(String(10))
    puntos = Column(Integer, default=0)
    two_pt_attempts = Column(Integer, default=0)
    two_pt_made = Column(Integer, default=0)
    two_pt_percentage = Column(String(5), default="0.0")
    three_pt_attempts = Column(Integer, default=0)
    three_pt_made = Column(Integer, default=0)
    three_pt_percentage = Column(String(5), default="0.0")
    total_attempts = Column(Integer, default=0)
    total_made = Column(Integer, default=0)
    fg_percentage = Column(String(5), default="0.0")
    ft_attempts = Column(Integer, default=0)
    ft_made = Column(Integer, default=0)
    ft_percentage = Column(String(5), default="0.0")
    asistencias = Column(Integer, default=0)
    robos = Column(Integer, default=0)
    tapones = Column(Integer, default=0)
    turnovers = Column(Integer, default=0)
    offensive_rebounds = Column(Integer, default=0)
    defensive_rebounds = Column(Integer, default=0)

    jugador = relationship("Player", back_populates="stats")
    match = relationship("Match", back_populates="stats")
    team = relationship("Team")