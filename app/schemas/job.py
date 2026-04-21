from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str
    company: str
    location: str
    description: str
    salary: Optional[str] = None
    skills: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }