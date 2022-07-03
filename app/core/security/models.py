"""
Models related to the security package.
"""
from pydantic import BaseModel


class TokenModel(BaseModel):
    """Token Model class."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token Data class"""
    id: str
