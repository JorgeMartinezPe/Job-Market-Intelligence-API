from pydantic import BaseModel
from datetime import datetime

class SkillsBase(BaseModel):
    id:int
    name:str

class SkillResponse(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }