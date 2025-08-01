from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class MatchBase(BaseModel):
    zona_id: int = Field(..., gt=0)
    local_team_id: int = Field(..., gt=0)
    away_team_id: int = Field(..., gt=0)
    fecha: date
    resultado: Optional[str] = None
    estado: Optional[str] = "pendiente"

class MatchCreate(MatchBase):
    torneo_id: int = Field(..., gt=0)

    class Config:
        orm_mode = True

class MatchOut(MatchBase):
    id: int

    class Config:
        orm_mode = True