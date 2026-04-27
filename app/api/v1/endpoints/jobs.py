from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.job import JobCreate,JobResponse
from app.models.job import Job
from app.models.companies_db import Company
from app.models.skill import Skill
from app.models.locations import Location

router = APIRouter()

@router.post("/crear_trabajo")
def create_job(job:JobCreate,db:Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == job.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
        
    location = db.query(Location).filter(Location.id == job.location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    new_job = Job(
        title = job.title,
        description = job.description,
        salary_max = job.salary_max,
        salary_min = job.salary_min,
        currency = job.currency,
        location_id = job.location_id,
        company_id = job.company_id

    )
    for skill_name in job.skills:
        skill = db.query(Skill).filter(Skill.name == skill_name.name).first()

        if not skill:
            skill = Skill(name=skill_name.name)
            db.add(skill)
            db.flush()  # para obtener id sin commit

        new_job.skills.append(skill)


    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job