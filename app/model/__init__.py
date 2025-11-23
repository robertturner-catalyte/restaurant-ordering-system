from .menuitem import *
from .order import *
from .orderitem import *


from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    """Base class for all ORM models."""
    pass


__all__ = ["BaseModel"]
