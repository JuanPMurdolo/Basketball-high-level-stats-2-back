from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    tipo = Column(String(20), nullable=False)  # Ej: "Mayores", "Menores"

    torneos = relationship("Tournament", back_populates="categoria")