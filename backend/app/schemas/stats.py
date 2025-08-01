from pydantic import BaseModel, Field
from typing import Optional

class StatBase(BaseModel):
    match_id: int = Field(..., gt=0)
    jugador_id: int = Field(..., gt=0)
    team_id: int = Field(..., gt=0)

    minutos: Optional[str] = Field(None, max_length=8)
    puntos: int = Field(0, ge=0)
    two_pt_attempts: int = Field(0, ge=0)
    two_pt_made: int = Field(0, ge=0)
    three_pt_attempts: int = Field(0, ge=0)
    three_pt_made: int = Field(0, ge=0)
    fta: int = Field(0, ge=0)
    ftm: int = Field(0, ge=0)
    asistencias: int = Field(0, ge=0)
    robos: int = Field(0, ge=0)
    tapones: int = Field(0, ge=0)
    turnovers: int = Field(0, ge=0)
    offensive_rebounds: int = Field(0, ge=0)
    defensive_rebounds: int = Field(0, ge=0)

class StatCreate(StatBase):
    pass

class StatOut(StatBase):
    id: int

    class Config:
        orm_mode = True

class StatAdvancedOut(BaseModel):
    jugador_id: int
    match_id: int
    team_id: int
    minutos: str
    puntos: int

    plays: float
    ppp: float
    efg: float
    ts: float
    ppt1: float
    ppt2: float
    ppt3: float
    oe: float
    eps: float

    class Config:
        orm_mode = True