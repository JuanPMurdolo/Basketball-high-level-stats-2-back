
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.db import Base
from datetime import datetime

class StatsPlayer(Base):
    __tablename__ = "stats_player"
    
    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"))
    stats_id = Column(Integer, ForeignKey("basketball_stats.id", ondelete="CASCADE"))

    jugador = relationship("Player", back_populates="stats_player")
    stats = relationship("BasketballStats", back_populates="stats_player")

    def __repr__(self):
        return f"<StatsPlayer(jugador_id={self.jugador_id}, stats_id={self.stats_id})>"