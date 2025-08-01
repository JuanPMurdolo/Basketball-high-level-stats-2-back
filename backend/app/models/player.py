from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String(50))
    equipo_id = Column(Integer, ForeignKey("teams.id", ondelete="SET NULL"))

    equipo = relationship("Team", back_populates="jugadores")
    stats = relationship("BasketballStats", back_populates="jugador")