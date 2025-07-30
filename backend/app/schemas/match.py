from pydantic import BaseModel
from datetime import date
from typing import Optional

class MatchBase(BaseModel):
    zona_id: int
    local_team_id: int
    away_team_id: int
    fecha: date
    resultado: Optional[str] = None
    estado: Optional[str] = "pendiente"

class MatchCreate(MatchBase):
    pass

class MatchOut(MatchBase):
    id: int

    class Config:
        orm_mode = True