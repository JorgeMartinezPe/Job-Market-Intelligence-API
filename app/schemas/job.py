from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.skill import SkillResponse
from app.schemas.locations import LocationCreate, LocationResponse
from app.schemas.companies import CompanyResponse


class JobBase(BaseModel):
    title: str
    description: Optional[str] = None

    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    currency: Optional[str] = None
    company_id: int
    location_id: Optional[int] = None
    location: Optional[LocationCreate] = None


class JobCreate(JobBase):
    skills: List[str]


class JobResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    currency: Optional[str] = None
    published_at: Optional[datetime] = None
    company: Optional[CompanyResponse] = None
    location: Optional[LocationResponse] = None
    skills: List[SkillResponse]

    model_config = {
        "from_attributes": True
    }


class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    currency: Optional[str] = None
    skills: Optional[List[str]] = None
