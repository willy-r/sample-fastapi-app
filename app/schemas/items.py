from typing import Optional

from pydantic import BaseModel


class CreateItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class UpdateItem(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
