from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import player as player_schema
from app.crud import player as player_crud

router = APIRouter(prefix="/jugadores", tags=["Jugadores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=player_schema.PlayerOut)
def crear_jugador(player: player_schema.PlayerCreate, db: Session = Depends(get_db)):
    return player_crud.create_player(db, player)

@router.get("/", response_model=list[player_schema.PlayerOut])
def listar_jugadores(db: Session = Depends(get_db)):
    return player_crud.get_all_players(db)

@router.get("/equipo/{equipo_id}/", response_model=list[player_schema.PlayerOut])
def jugadores_por_equipo(equipo_id: int, db: Session = Depends(get_db)):
    return player_crud.get_players_by_team(db, equipo_id)