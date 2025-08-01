from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.db import Base

class ZoneTeam(Base):
    __tablename__ = "zone_teams"

    id = Column(Integer, primary_key=True, index=True)
    zona_id = Column(Integer, ForeignKey("zones.id"))
    equipo_id = Column(Integer, ForeignKey("teams.id"))

    zona = relationship("Zone", back_populates="equipos")
    equipo = relationship("Team", back_populates="zone_teams")