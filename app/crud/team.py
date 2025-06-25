from sqlalchemy.orm import Session
from app import models, schemas

# --- TEAM ---

def create_team(db: Session, team: schemas.team.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session):
    return db.query(models.Team).all()


# --- ZONE TEAM ---

def assign_team_to_zone(db: Session, assignment: schemas.team.ZoneTeamCreate):
    db_zone_team = models.ZoneTeam(**assignment.dict())
    db.add(db_zone_team)
    db.commit()
    db.refresh(db_zone_team)
    return db_zone_team

def get_teams_by_zone(db: Session, zona_id: int):
    return db.query(models.ZoneTeam).filter(models.ZoneTeam.zona_id == zona_id).all()