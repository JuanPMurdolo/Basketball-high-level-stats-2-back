from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class TournamentBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=40)
    categoria_id: int = Field(..., gt=0)
    fecha_inicio: date
    fecha_fin: Optional[date] = None

class TournamentCreate(TournamentBase):
    pass

class TournamentOut(TournamentBase):
    id: int

    class Config:
        orm_mode = True