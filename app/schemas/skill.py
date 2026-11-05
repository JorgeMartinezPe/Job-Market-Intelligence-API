from pydantic import BaseModel
from typing import Optional

class SkillResponse(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

class SkillCreate(BaseModel):
    name:str

class SkillUpdate(BaseModel):
    name: Optional[str] = None

