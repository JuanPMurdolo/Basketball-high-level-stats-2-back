from pydantic import BaseModel
from datetime import date

class CategoryBase(BaseModel):
    nombre: str
    tipo: str  # "Mayores", "Menores", "Premini"

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True