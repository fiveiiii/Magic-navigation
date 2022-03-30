from typing import Optional, List
from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: int = None
    message: str = None
