from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional, List
from app.schemas.skill import SkillResponse
from app.schemas.locations import LocationCreate, LocationResponse


class JobBase(BaseModel):
    title: str
    description: Optional[str] = None

    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    annual_salary: Optional[float] = None
    currency: Optional[str] = None
    company_id: Optional[int] = None
    external_id: Optional[str] = None
    job_category: Optional[str] = None
    experience_level: Optional[str] = None
    years_of_experience: Optional[int] = None
    education_required: Optional[str] = None
    remote_work: Optional[str] = None
    posting_year: Optional[int] = None
    posting_month: Optional[int] = Field(default=None, ge=1, le=12)
    ai_salary_premium_pct: Optional[float] = None
    demand_score: Optional[float] = None
    demand_growth_yoy_pct: Optional[float] = None
    benefits_score: Optional[float] = None
    is_llm_role: Optional[bool] = None


class JobCreate(JobBase):
    location_id: Optional[int] = None
    location: Optional[LocationCreate] = None
    skills: List[str] = []

    @model_validator(mode="after")
    def check_location(self):
        if self.location_id is None and self.location is None:
            raise ValueError("Either location_id or location is required")
        return self


class JobResponse(JobBase):
    id: int
    published_at: Optional[datetime] = None
    location_id: Optional[int] = None
    location: Optional[LocationResponse] = None
    skills: List[SkillResponse] = []
    model_config = {
        "from_attributes": True
    }


class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    annual_salary: Optional[float] = None
    currency: Optional[str] = None
    job_category: Optional[str] = None
    experience_level: Optional[str] = None
    years_of_experience: Optional[int] = None
    education_required: Optional[str] = None
    remote_work: Optional[str] = None
    posting_year: Optional[int] = None
    posting_month: Optional[int] = Field(default=None, ge=1, le=12)
    ai_salary_premium_pct: Optional[float] = None
    demand_score: Optional[float] = None
    demand_growth_yoy_pct: Optional[float] = None
    benefits_score: Optional[float] = None
    is_llm_role: Optional[bool] = None
    skills: Optional[List[str]] = None
