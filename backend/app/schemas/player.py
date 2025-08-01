from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class PlayerBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=40)
    apellido: str = Field(..., min_length=2, max_length=40)
    fecha_nacimiento: Optional[date] = None

class PlayerCreate(PlayerBase):
    equipo_id: int = Field(..., gt=0)

class PlayerOut(PlayerBase):
    id: int

    class Config:
        orm_mode = True