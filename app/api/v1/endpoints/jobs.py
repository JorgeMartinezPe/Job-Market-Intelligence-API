from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.job import Job, JobCreate
from app.services.job_service import JobService

router = APIRouter()

@router.post("/", response_model=Job)
def create_job():
    pass # en proceso