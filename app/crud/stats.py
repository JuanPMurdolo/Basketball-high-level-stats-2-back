from sqlalchemy.orm import Session
from app import models, schemas

def create_stat(db: Session, stat: schemas.stats.StatCreate):
    db_stat = models.BasketballStats(**stat.dict())
    db.add(db_stat)
    db.commit()
    db.refresh(db_stat)
    return db_stat

def get_stats_by_match(db: Session, match_id: int):
    return db.query(models.BasketballStats).filter(models.BasketballStats.match_id == match_id).all()

def get_stats_by_player(db: Session, jugador_id: int):
    return db.query(models.BasketballStats).filter(models.BasketballStats.jugador_id == jugador_id).all()