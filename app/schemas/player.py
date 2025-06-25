from pydantic import BaseModel
from typing import Optional

class PlayerBase(BaseModel):
    nombre: str
    dorsal: Optional[int] = None
    posicion: Optional[str] = None
    equipo_id: Optional[int] = None

class PlayerCreate(PlayerBase):
    pass

class PlayerOut(PlayerBase):
    id: int

    class Config:
        orm_mode = True