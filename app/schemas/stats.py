from pydantic import BaseModel
from typing import Optional
from app.utils.advanced_metrics import *

class StatBase(BaseModel):
    match_id: int
    jugador_id: int
    team_id: int

    minutos: Optional[str] = None
    puntos: int = 0
    two_pt_attempts: int = 0
    two_pt_made: int = 0
    three_pt_attempts: int = 0
    three_pt_made: int = 0
    fta: int = 0
    ftm: int = 0
    asistencias: int = 0
    robos: int = 0
    tapones: int = 0
    turnovers: int = 0
    offensive_rebounds: int = 0
    defensive_rebounds: int = 0

class StatCreate(StatBase):
    pass

class StatOut(StatBase):
    id: int

    class Config:
        orm_mode = True
        
class StatOut(StatBase):
    id: int

    class Config:
        orm_mode = True

    @property
    def fga(self):
        return self.two_pt_attempts + self.three_pt_attempts

    @property
    def fgm(self):
        return self.two_pt_made + self.three_pt_made

    @property
    def plays(self):
        return plays(self.two_pt_attempts, self.three_pt_attempts, self.fta, self.turnovers)

    @property
    def ppp(self):
        return ppp(self.puntos, self.plays)

    @property
    def efg(self):
        return efg(self.fgm, self.three_pt_made, self.fga)

    @property
    def ts(self):
        return ts(self.fga, self.fta, self.puntos)

    @property
    def ppt1(self):
        return ppt1(self.fta, self.ftm)

    @property
    def ppt2(self):
        return ppt2(self.two_pt_attempts, self.two_pt_made)

    @property
    def ppt3(self):
        return ppt3(self.three_pt_attempts, self.three_pt_made)

    @property
    def oe(self):
        return oe(self.fga, self.offensive_rebounds, self.asistencias, self.turnovers, self.fgm)

    @property
    def eps(self):
        return eps(self.puntos, self.oe)

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