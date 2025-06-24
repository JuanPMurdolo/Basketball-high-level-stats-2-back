from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import base, tournament as tournament_schema
from app.crud import tournament as tournament_crud

router = APIRouter(prefix="/torneos", tags=["Torneos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- CATEGORÍAS -----

@router.post("/categorias/", response_model=base.CategoryOut)
def crear_categoria(category: base.CategoryCreate, db: Session = Depends(get_db)):
    return tournament_crud.create_category(db, category)

@router.get("/categorias/", response_model=list[base.CategoryOut])
def listar_categorias(db: Session = Depends(get_db)):
    return tournament_crud.get_categories(db)


# ----- TORNEOS -----

@router.post("/", response_model=tournament_schema.TournamentOut)
def crear_torneo(tour: tournament_schema.TournamentCreate, db: Session = Depends(get_db)):
    return tournament_crud.create_tournament(db, tour)

@router.get("/", response_model=list[tournament_schema.TournamentOut])
def listar_torneos(db: Session = Depends(get_db)):
    return tournament_crud.get_tournaments(db)


# ----- FASES -----

@router.post("/fases/", response_model=tournament_schema.PhaseOut)
def crear_fase(phase: tournament_schema.PhaseCreate, db: Session = Depends(get_db)):
    return tournament_crud.create_phase(db, phase)

@router.get("/{tournament_id}/fases/", response_model=list[tournament_schema.PhaseOut])
def fases_por_torneo(tournament_id: int, db: Session = Depends(get_db)):
    return tournament_crud.get_phases_by_tournament(db, tournament_id)


# ----- ZONAS -----

@router.post("/zonas/", response_model=tournament_schema.ZoneOut)
def crear_zona(zone: tournament_schema.ZoneCreate, db: Session = Depends(get_db)):
    return tournament_crud.create_zone(db, zone)

@router.get("/fases/{phase_id}/zonas/", response_model=list[tournament_schema.ZoneOut])
def zonas_por_fase(phase_id: int, db: Session = Depends(get_db)):
    return tournament_crud.get_zones_by_phase(db, phase_id)
