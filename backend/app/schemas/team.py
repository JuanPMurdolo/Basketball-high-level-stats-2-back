from pydantic import BaseModel, Field
from typing import Optional

class TeamBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    ciudad: Optional[str] = Field(None, max_length=100)

class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    ciudad: Optional[str] = Field(None, max_length=100)

class TeamOut(TeamBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True