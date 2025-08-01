from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    anio = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categories.id"))

    categoria = relationship("Category", back_populates="torneos")
    fases = relationship("Phase", back_populates="torneo")