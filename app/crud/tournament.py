from sqlalchemy.orm import Session
from app import models, schemas

# --------- CATEGORIES ---------

def create_category(db: Session, category: schemas.base.CategoryCreate):
    db_cat = models.Category(**category.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def get_categories(db: Session):
    return db.query(models.Category).all()


# --------- TOURNAMENTS ---------

def create_tournament(db: Session, tournament: schemas.tournament.TournamentCreate):
    db_tour = models.Tournament(**tournament.dict())
    db.add(db_tour)
    db.commit()
    db.refresh(db_tour)
    return db_tour

def get_tournaments(db: Session):
    return db.query(models.Tournament).all()

def get_tournament(db: Session, tournament_id: int):
    return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()


# --------- PHASES ---------

def create_phase(db: Session, phase: schemas.tournament.PhaseCreate):
    db_phase = models.Phase(**phase.dict())
    db.add(db_phase)
    db.commit()
    db.refresh(db_phase)
    return db_phase

def get_phases_by_tournament(db: Session, tournament_id: int):
    return db.query(models.Phase).filter(models.Phase.torneo_id == tournament_id).all()


# --------- ZONES ---------

def create_zone(db: Session, zone: schemas.tournament.ZoneCreate):
    db_zone = models.Zone(**zone.dict())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone

def get_zones_by_phase(db: Session, phase_id: int):
    return db.query(models.Zone).filter(models.Zone.fase_id == phase_id).all()
