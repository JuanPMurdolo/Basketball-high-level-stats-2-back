from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(10))  # A1, B2, etc.
    fase_id = Column(Integer, ForeignKey("phases.id"))

    fase = relationship("Phase", back_populates="zonas")
    equipos = relationship("ZoneTeam", back_populates="zona")
    partidos = relationship("Match", back_populates="zona")