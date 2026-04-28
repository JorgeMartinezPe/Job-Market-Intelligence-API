from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.skill_service import get_or_create_skills
from app.services.location_service import get_or_create_location
from app.schemas.job import JobCreate,JobResponse,JobUpdate
from app.models.job import Job
from app.models.companies_db import Company
from app.models.skill import Skill
from app.models.locations import Location
from typing import Annotated
router = APIRouter()

@router.post("/crear_trabajo")
def create_job(job: JobCreate, db: Annotated[Session, Depends(get_db)]):

    # validar company
    company = db.query(Company).filter(Company.id == job.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    # resolver location
    if job.location_id:
        location = db.query(Location).filter(Location.id == job.location_id).first()
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        location_id = location.id

    elif job.location:
        location = get_or_create_location(
            db,
            country=job.location.country,
            state=job.location.state,
            city=job.location.city
        )
        location_id = location.id

    else:
        raise HTTPException(status_code=400, detail="Location is required")

    # crear job
    new_job = Job(
        title=job.title,
        description=job.description,
        salary_max=job.salary_max,
        salary_min=job.salary_min,
        currency=job.currency,
        location_id=location_id,  # ✅ corregido
        company_id=job.company_id
    )

    # skills
    skills = get_or_create_skills(db, job.skills)
    new_job.skills = skills

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job

@router.get("/all_jobs", response_model=list[JobResponse])
def get_jobs(db: Annotated[Session, Depends(get_db)]):
    jobs = db.query(Job).all()

    return jobs


@router.get("/jobs_by_id{id}",response_model=JobResponse)
def get_jobs_by_id(id:int,db: Annotated[Session, Depends(get_db)]):
    job = db.query(Job).filter(Job.id==id).first()
    return job

#Update
@router.post("/update_job{id}")
def update_job(id:int,job:JobUpdate,db: Annotated[Session, Depends(get_db)]):
    job_db = db.query(Job).filter(Job.id==id).first()
    if job_db is None:
        raise HTTPException(status_code=404, detail="Job not found")
    job_db.title = job.title
    job_db.description = job.description
    job_db.salary_max = job.salary_max
    job_db.salary_min = job.salary_min
    skills = get_or_create_skills(db, job.skills)
    job_db.skills = skills

    db.commit()
    db.refresh(job_db)
    return "Actualizado con exito"

#Delete
@router.delete("/delete_job{id}")
def delete_job(id:int,db: Annotated[Session, Depends(get_db)]):
    job_db = db.query(Job).filter(Job.id==id).first()
    if job_db is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job_db)
    db.commit()
    return "Eliminado con exito"