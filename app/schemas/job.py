from pydantic import BaseModel
from typing import Optional,List
from app.schemas.skill import SkillResponse
class JobBase(BaseModel):
    title: str
    description: Optional[str] = None

    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    currency:   Optional[str] = None
    company_id: int
    location_id: int

    skills: List[SkillResponse]

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id:int
    model_config = {
        "from_attributes": True
    }