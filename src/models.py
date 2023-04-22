from typing import List
from pydantic import BaseModel


class City(BaseModel):
    name: str
    location: List[float]
