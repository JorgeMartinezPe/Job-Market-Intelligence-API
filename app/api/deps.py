"""Wiring de inyección de dependencias: DB -> Repositories -> Services.

Los routers solo dependen de las funciones `get_*_service` de aquí abajo;
nunca importan `Session` ni los repositorios directamente.
"""
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.company_repository import CompanyRepository
from app.repositories.job_repository import JobRepository
from app.repositories.location_repository import LocationRepository
from app.repositories.skill_repository import SkillRepository
from app.services.company_service import CompanyService
from app.services.job_service import JobService
from app.services.location_service import LocationService
from app.services.skill_service import SkillService
from app.repositories.country_repository import CountryRepository
from app.services.country_service import CountryService

DbSession = Annotated[Session, Depends(get_db)]


def get_job_repository(db: DbSession) -> JobRepository:
    return JobRepository(db)


def get_company_repository(db: DbSession) -> CompanyRepository:
    return CompanyRepository(db)


def get_location_repository(db: DbSession) -> LocationRepository:
    return LocationRepository(db)


def get_skill_repository(db: DbSession) -> SkillRepository:
    return SkillRepository(db)

def get_country_repository(db:DbSession)-> CountryRepository:
    return CountryRepository(db)

def get_location_repository(db:DbSession)-> LocationRepository:
    return LocationRepository(db)


def get_location_service(
    repository: Annotated[LocationRepository, Depends(get_location_repository)],
) -> LocationService:
    return LocationService(repository)


def get_skill_service(
    repository: Annotated[SkillRepository, Depends(get_skill_repository)],
) -> SkillService:
    return SkillService(repository)


def get_job_service(
    job_repository: Annotated[JobRepository, Depends(get_job_repository)],
    company_repository: Annotated[CompanyRepository, Depends(get_company_repository)],
    location_repository: Annotated[LocationRepository, Depends(get_location_repository)],
    location_service: Annotated[LocationService, Depends(get_location_service)],
    skill_service: Annotated[SkillService, Depends(get_skill_service)],
) -> JobService:
    return JobService(
        job_repository=job_repository,
        company_repository=company_repository,
        location_repository=location_repository,
        location_service=location_service,
        skill_service=skill_service,
    )


def get_company_service(
    repository: Annotated[CompanyRepository, Depends(get_company_repository)],
) -> CompanyService:
    return CompanyService(repository)

def get_country_service(
        repository: Annotated[CountryRepository, Depends(get_country_repository)],
)->CountryService:
    return CountryService(repository)
