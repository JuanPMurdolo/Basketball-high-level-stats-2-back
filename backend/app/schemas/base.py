from datetime import date
from typing import Optional
from pydantic import Field, BaseModel

class CategoryBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=20)
    tipo: str = Field(..., min_length=2, max_length=20)  # Ej: "Mayores", "Menores"

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True