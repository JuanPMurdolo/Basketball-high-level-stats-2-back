from sqlalchemy.orm import Session
from app import models, schemas

def create_player(db: Session, player: schemas.player.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_players_by_team(db: Session, equipo_id: int):
    return db.query(models.Player).filter(models.Player.equipo_id == equipo_id).all()

def get_all_players(db: Session):
    return db.query(models.Player).all()