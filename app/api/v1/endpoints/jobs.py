from typing import Annotated, List

from fastapi import APIRouter, Depends

from app.api.deps import get_job_service
from app.schemas.job import JobCreate, JobResponse, JobUpdate
from app.services.job_service import JobService

router = APIRouter()

<<<<<<< HEAD
JobServiceDep = Annotated[JobService, Depends(get_job_service)]


@router.post("/", response_model=JobResponse, status_code=201)
def create_job(job: JobCreate, service: JobServiceDep):
    return service.create_job(job)


@router.get("/", response_model=List[JobResponse])
def get_jobs(service: JobServiceDep):
    return service.get_all()


@router.get("/{id}", response_model=JobResponse)
def get_job_by_id(id: int, service: JobServiceDep):
    return service.get_by_id(id)


@router.put("/{id}", response_model=JobResponse)
def update_job(id: int, job: JobUpdate, service: JobServiceDep):
    return service.update_job(id, job)
=======
@router.post("/crear_trabajo",response_model=JobResponse)
def create_job(job: JobCreate, db: Annotated[Session, Depends(get_db)]):

    # validar company (opcional)
    if job.company_id is not None:
        company = db.query(Company).filter(Company.id == job.company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")

    # resolver location
    if job.location_id is not None:
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
        **job.model_dump(exclude={"location", "location_id", "skills"}),
        location_id=location_id,
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
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")
    

    return jobs


@router.get("/jobs_by_id/{id}",response_model=JobResponse)
def get_jobs_by_id(id:int,db: Annotated[Session, Depends(get_db)]):
    job = db.query(Job).filter(Job.id==id).first()
    if not job:
        raise HTTPException(status_code=404,detail="No existe un trabajo con este id")
    return job

#Update
@router.put("/update_job/{id}",response_model=JobResponse)
def update_job(id:int,job:JobUpdate,db: Annotated[Session, Depends(get_db)]):
    job_db = db.query(Job).filter(Job.id==id).first()
    if job_db is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Solo se modifican los campos enviados
    for field, value in job.model_dump(exclude_unset=True, exclude={"skills"}).items():
        setattr(job_db, field, value)

    if job.skills is not None:
        job_db.skills = get_or_create_skills(db, job.skills)
>>>>>>> eccfe6b12233fb220f13d162ecbea7c7868cc263


<<<<<<< HEAD
@router.delete("/{id}", status_code=204)
def delete_job(id: int, service: JobServiceDep):
    service.delete_job(id)
=======
#Delete
@router.delete("/delete_job/{id}")
def delete_job(id:int,db: Annotated[Session, Depends(get_db)]):
    job_db = db.query(Job).filter(Job.id==id).first()
    if job_db is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job_db)
    db.commit()
    return "Eliminado con exito"
>>>>>>> eccfe6b12233fb220f13d162ecbea7c7868cc263
