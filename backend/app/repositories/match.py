from sqlalchemy.orm import Session
from app.models import Match
from app.schemas.match import MatchCreate
from app.core.logging import logger

Logger = logger.getChild(__name__)


class MatchRepository:
    def __init__(self, db: Session):
        """Initialize the MatchRepository with a database session."""
        Logger.debug("Initializing MatchRepository")
        if db is None:
            raise ValueError("Database session cannot be None")
        Logger.debug("Database session provided")
        self.db = db

    def create_match(self, match: MatchCreate) -> Match:
        try:
            db_match = Match(**match.dict())
            self.db.add(db_match)
            self.db.commit()
            self.db.refresh(db_match)
            logger.info(f"Match created with ID {db_match.id}")
            return db_match
        except Exception as e:
            logger.error(f"Error creating match: {e}")
            self.db.rollback()
            raise

    def get_matches_by_zone(self, zona_id: int) -> list[Match]:
        try:
            matches = self.db.query(Match).filter(Match.zona_id == zona_id).all()
            logger.info(f"Fetched {len(matches)} matches for zone {zona_id}")
            return matches
        except Exception as e:
            logger.error(f"Error fetching matches by zone: {e}")
            return []