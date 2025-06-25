from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import stats as stats_schema
from app.crud import stats as stats_crud
from app.utils.advanced_metrics import (
    plays, ppp, efg, ts, ppt1, ppt2, ppt3, oe, eps
)


router = APIRouter(prefix="/stats", tags=["Estadísticas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=stats_schema.StatOut)
def crear_stat(stat: stats_schema.StatCreate, db: Session = Depends(get_db)):
    return stats_crud.create_stat(db, stat)

@router.get("/match/{match_id}/", response_model=list[stats_schema.StatOut])
def stats_por_partido(match_id: int, db: Session = Depends(get_db)):
    return stats_crud.get_stats_by_match(db, match_id)

@router.get("/player/{jugador_id}/", response_model=list[stats_schema.StatOut])
def stats_por_jugador(jugador_id: int, db: Session = Depends(get_db)):
    return stats_crud.get_stats_by_player(db, jugador_id)

@router.get("/match/{match_id}/advanced/", response_model=list[stats_schema.StatAdvancedOut])
def advanced_stats(match_id: int, db: Session = Depends(get_db)):
    raw_stats = stats_crud.get_stats_by_match(db, match_id)
    result = []

    for s in raw_stats:
        fga = s.two_pt_attempts + s.three_pt_attempts
        fgm = s.two_pt_made + s.three_pt_made
        p = plays(s.two_pt_attempts, s.three_pt_attempts, s.fta, s.turnovers)
        res = {
            "jugador_id": s.jugador_id,
            "match_id": s.match_id,
            "team_id": s.team_id,
            "minutos": s.minutos,
            "puntos": s.puntos,
            "plays": p,
            "ppp": ppp(s.puntos, p),
            "efg": efg(fgm, s.three_pt_made, fga),
            "ts": ts(fga, s.fta, s.puntos),
            "ppt1": ppt1(s.fta, s.ftm),
            "ppt2": ppt2(s.two_pt_attempts, s.two_pt_made),
            "ppt3": ppt3(s.three_pt_attempts, s.three_pt_made),
            "oe": oe(fga, s.offensive_rebounds, s.asistencias, s.turnovers, fgm),
            "eps": eps(s.puntos, oe(fga, s.offensive_rebounds, s.asistencias, s.turnovers, fgm))
        }
        result.append(res)
    return result