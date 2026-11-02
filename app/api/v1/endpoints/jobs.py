from typing import Annotated, List

from fastapi import APIRouter, Depends

from app.api.deps import get_job_service
from app.schemas.job import JobCreate, JobResponse, JobUpdate
from app.services.job_service import JobService

router = APIRouter()

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


@router.delete("/{id}", status_code=204)
def delete_job(id: int, service: JobServiceDep):
    service.delete_job(id)
