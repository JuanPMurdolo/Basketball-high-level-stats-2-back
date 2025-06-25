from sqlalchemy.orm import Session
from app import models, schemas

def create_match(db: Session, match: schemas.match.MatchCreate):
    db_match = models.Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def get_matches_by_zona(db: Session, zona_id: int):
    return db.query(models.Match).filter(models.Match.zona_id == zona_id).all()