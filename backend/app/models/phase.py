from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Phase(Base):
    __tablename__ = "phases"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))  # "Apertura", "Clausura", "Anual"
    inicio = Column(Date)
    fin = Column(Date)
    torneo_id = Column(Integer, ForeignKey("tournaments.id"))

    torneo = relationship("Tournament", back_populates="fases")
    zonas = relationship("Zone", back_populates="fase")