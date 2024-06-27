import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer, Boolean
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import ColumnProperty, InstrumentedAttribute

def generate_uuid():
    return str(uuid.uuid4())

@as_declarative()
class Base:

    __abstract__ = True

    id = Column(String, primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def get_attribute_names(cls):
        return [
            a.key
            for a in [getattr(cls, k) for k in dir(cls)]
            if (
                isinstance(a, InstrumentedAttribute)
                and isinstance(a.property, ColumnProperty)
            )
        ]
    
    '''this method iterates over all attributes of a class, filters out those that are mapped to database columns (using specific criteria related to ORM), 
    and returns a list of their names. This can be particularly useful for dynamically generating queries or reports based on the class's schema.'''