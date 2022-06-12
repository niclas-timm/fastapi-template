# -------------------------------------------------------------------------------
# Pydantic schemas for slack message handling.
# -------------------------------------------------------------------------------
from pydantic import BaseModel


class SlackMessageBlockText(BaseModel):
    type: str
    text: str


class SlackMessageBlock(BaseModel):
    type: str
    text: SlackMessageBlockText