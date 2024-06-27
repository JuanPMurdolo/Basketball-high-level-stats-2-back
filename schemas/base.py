from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Base(BaseModel):
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    public_id: Optional[str]

    class Config:
        orm_mode = True
        