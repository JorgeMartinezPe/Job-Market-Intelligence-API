from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.skill_service import get_or_create_skills
from app.schemas.job import JobCreate,JobResponse,JobUpdate
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
    new_job = Job( #No usar JobCreate, siempre el modelo de la base de datos, el JobCreate es el schema guia.
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

@router.get("/all_jobs", response_model=list[JobResponse])
def get_jobs(db:Session = Depends(get_db)):
    jobs = db.query(Job).all()

    return jobs


@router.get("/jobs_by_id{id}",response_model=JobResponse)
def get_jobs_by_id(id:int,db:Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id==id).first()
    return job

#Update
@router.post("/update_job{id}")
def update_job(id:int,job:JobUpdate,db:Session = Depends(get_db)):
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