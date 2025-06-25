from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import team as team_schema
from app.crud import team as team_crud

router = APIRouter(prefix="/equipos", tags=["Equipos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- EQUIPOS ---

@router.post("/", response_model=team_schema.TeamOut)
def crear_equipo(team: team_schema.TeamCreate, db: Session = Depends(get_db)):
    return team_crud.create_team(db, team)

@router.get("/", response_model=list[team_schema.TeamOut])
def listar_equipos(db: Session = Depends(get_db)):
    return team_crud.get_teams(db)

# --- ASIGNACIÓN A ZONA ---

@router.post("/asignar_zona/", response_model=team_schema.ZoneTeamOut)
def asignar_equipo_a_zona(asignacion: team_schema.ZoneTeamCreate, db: Session = Depends(get_db)):
    return team_crud.assign_team_to_zone(db, asignacion)

@router.get("/zonas/{zona_id}/equipos", response_model=list[team_schema.ZoneTeamOut])
def equipos_por_zona(zona_id: int, db: Session = Depends(get_db)):
    return team_crud.get_teams_by_zone(db, zona_id)