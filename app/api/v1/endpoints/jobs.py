from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.job import Job, JobCreate
from app.services.job_service import JobService

router = APIRouter()

def get_job_service(db: Session = Depends(get_db)):
    return JobService(db)

@router.get("/", response_model=list[Job])
def get_jobs(service: JobService = Depends(get_job_service)):
    return service.get_all_jobs()

@router.post("/", response_model=Job)
def create_job(job: JobCreate, service: JobService = Depends(get_job_service)):
    return service.create_job(job)