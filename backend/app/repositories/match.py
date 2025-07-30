from sqlalchemy.orm import Session
from app.models import Match
from app.schemas.match import MatchCreate


class MatchRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_match(self, match: MatchCreate):
        db_match = Match(**match.dict())
        self.db.add(db_match)
        self.db.commit()
        self.db.refresh(db_match)
        return db_match

    def get_matches_by_zone(self, zona_id: int):
        return self.db.query(Match).filter(Match.zona_id == zona_id).all()