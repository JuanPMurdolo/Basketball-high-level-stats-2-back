from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    zona_id = Column(Integer, ForeignKey("zones.id"))
    fecha = Column(Date, default=datetime.utcnow)
    local_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))
    resultado = Column(String(20))
    estado = Column(String(20), default="pendiente")

    zona = relationship("Zone", back_populates="partidos")
    local_team = relationship("Team", foreign_keys=[local_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
    stats = relationship("BasketballStats", back_populates="match")