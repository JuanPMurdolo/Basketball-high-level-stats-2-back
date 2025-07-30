from sqlalchemy.orm import Session
from app.models import BasketballStats
from app.schemas import StatsCreate

class StatsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_stats(self, stats: StatsCreate):
        db_stats = BasketballStats(**stats.dict())
        self.db.add(db_stats)
        self.db.commit()
        self.db.refresh(db_stats)
        return db_stats

    def get_stats_by_match(self, match_id: int):
        return self.db.query(BasketballStats).filter(BasketballStats.match_id == match_id).all()

    def get_stats_by_player(self, player_id: int):
        return self.db.query(BasketballStats).filter(BasketballStats.player_id == player_id).all()