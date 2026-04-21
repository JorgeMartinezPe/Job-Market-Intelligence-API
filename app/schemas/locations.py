from pydantic import BaseModel
from typing import Optional


class LocationCreate(BaseModel):
    country:str
    state:Optional[str] = None
    city:Optional[str] = None

class LocationResponse(BaseModel):
    id:int
    country:str
    state:Optional[str] = None
    city:Optional[str] = None
    model_config = {
        "from_attributes": True
    }

class LocationUpdate(BaseModel):
    country:Optional[str] = None
    state:Optional[str] = None
    city:Optional[str] = None