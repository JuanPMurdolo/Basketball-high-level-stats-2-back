from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from .base import CategoryOut

class TournamentBase(BaseModel):
    nombre: str
    anio: int
    categoria_id: int

class TournamentCreate(TournamentBase):
    pass

class TournamentOut(TournamentBase):
    id: int
    categoria: Optional[CategoryOut]

    class Config:
        orm_mode = True


class PhaseBase(BaseModel):
    nombre: str
    inicio: date
    fin: date
    torneo_id: int

class PhaseCreate(PhaseBase):
    pass

class PhaseOut(PhaseBase):
    id: int

    class Config:
        orm_mode = True


class ZoneBase(BaseModel):
    nombre: str
    fase_id: int

class ZoneCreate(ZoneBase):
    pass

class ZoneOut(ZoneBase):
    id: int

    class Config:
        orm_mode = True
