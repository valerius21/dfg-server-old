from typing import Optional

from pydantic import BaseModel


class Submission(BaseModel):
    """Submission Model from the frontend"""
    sensitivity: str
    is_private: bool
    photo_id: int
    uid: str
    acquaintance: Optional[bool] = False
    colleagues: Optional[bool] = False
    family: Optional[bool] = False
    friends: Optional[bool] = False
    everybody: Optional[bool] = False
    nobody: Optional[bool] = False
