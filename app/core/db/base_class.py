"""
Declare structure of the base class for sqlalchemy.
"""

from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Base class."""
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(self, cls) -> str:
        """Table name converting convention."""
        return cls.__name__.lower()
