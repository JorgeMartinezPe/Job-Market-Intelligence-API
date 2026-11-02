from typing import List

from app.core.exceptions import NotFoundError, ValidationError
from app.models.job import Job
from app.repositories.company_repository import CompanyRepository
from app.repositories.job_repository import JobRepository
from app.repositories.location_repository import LocationRepository
from app.schemas.job import JobCreate, JobUpdate
from app.services.location_service import LocationService
from app.services.skill_service import SkillService


class JobService:
    """Orquesta las reglas de negocio de Job. No conoce SQLAlchemy
    directamente: delega toda persistencia en los repositorios."""

    def __init__(
        self,
        job_repository: JobRepository,
        company_repository: CompanyRepository,
        location_repository: LocationRepository,
        location_service: LocationService,
        skill_service: SkillService,
    ):
        self.job_repository = job_repository
        self.company_repository = company_repository
        self.location_repository = location_repository
        self.location_service = location_service
        self.skill_service = skill_service

    def create_job(self, data: JobCreate) -> Job:
        company = self.company_repository.get(data.company_id)
        if not company:
            raise NotFoundError("Company not found")

        location_id = self._resolve_location_id(data)

        new_job = Job(
            title=data.title,
            description=data.description,
            salary_max=data.salary_max,
            salary_min=data.salary_min,
            currency=data.currency,
            location_id=location_id,
            company_id=data.company_id,
        )
        new_job.skills = self.skill_service.get_or_create_many(data.skills)

        self.job_repository.add(new_job)
        self.job_repository.commit()
        self.job_repository.refresh(new_job)
        return new_job

    def _resolve_location_id(self, data: JobCreate) -> int:
        if data.location_id:
            location = self.location_repository.get(data.location_id)
            if not location:
                raise NotFoundError("Location not found")
            return location.id

        if data.location:
            location = self.location_service.get_or_create(
                country=data.location.country,
                state=data.location.state,
                city=data.location.city,
            )
            return location.id

        raise ValidationError("Location is required")

    def get_all(self) -> List[Job]:
        return self.job_repository.get_all()

    def get_by_id(self, job_id: int) -> Job:
        job = self.job_repository.get(job_id)
        if not job:
            raise NotFoundError("No existe un trabajo con este id")
        return job

    def update_job(self, job_id: int, data: JobUpdate) -> Job:
        job = self.get_by_id(job_id)

        if data.title is not None:
            job.title = data.title
        if data.description is not None:
            job.description = data.description
        if data.salary_min is not None:
            job.salary_min = data.salary_min
        if data.salary_max is not None:
            job.salary_max = data.salary_max
        if data.skills is not None:
            job.skills = self.skill_service.get_or_create_many(data.skills)

        self.job_repository.commit()
        self.job_repository.refresh(job)
        return job

    def delete_job(self, job_id: int) -> None:
        job = self.get_by_id(job_id)
        self.job_repository.delete(job)
        self.job_repository.commit()
