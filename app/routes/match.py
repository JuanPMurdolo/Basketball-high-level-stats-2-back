from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import match as match_schema
from app.crud import match as match_crud

router = APIRouter(prefix="/partidos", tags=["Partidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=match_schema.MatchOut)
def crear_partido(match: match_schema.MatchCreate, db: Session = Depends(get_db)):
    return match_crud.create_match(db, match)

@router.get("/zona/{zona_id}/", response_model=list[match_schema.MatchOut])
def listar_partidos_por_zona(zona_id: int, db: Session = Depends(get_db)):
    return match_crud.get_matches_by_zona(db, zona_id)
