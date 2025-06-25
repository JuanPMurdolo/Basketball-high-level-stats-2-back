from pydantic import BaseModel

# --- TEAM ---

class TeamBase(BaseModel):
    nombre: str

class TeamCreate(TeamBase):
    pass

class TeamOut(TeamBase):
    id: int

    class Config:
        orm_mode = True


# --- ZONE TEAM ---

class ZoneTeamBase(BaseModel):
    zona_id: int
    equipo_id: int

class ZoneTeamCreate(ZoneTeamBase):
    pass

class ZoneTeamOut(ZoneTeamBase):
    id: int

    class Config:
        orm_mode = True