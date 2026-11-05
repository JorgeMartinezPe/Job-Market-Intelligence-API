from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.deps import get_company_service
from app.schemas.companies import CompanyCreate, CompanyResponse, CompanyUpdate
from app.services.company_service import CompanyService

router = APIRouter()

CompanyServiceDep = Annotated[CompanyService, Depends(get_company_service)]


@router.post("/", response_model=CompanyResponse, status_code=200)
def create_company(company: CompanyCreate, service: CompanyServiceDep):
    return service.create(company)


@router.get("/{id}", response_model=CompanyResponse)
def get_company(id: int, service: CompanyServiceDep):
    return service.get_by_id(id)


@router.put("/{id}", response_model=CompanyResponse)
def update_company(id: int, company: CompanyUpdate, service: CompanyServiceDep):
    return service.update(id, company)


@router.delete("/{id}", response_model=CompanyResponse)
def delete_company(id: int, service: CompanyServiceDep):
    return service.delete(id)
