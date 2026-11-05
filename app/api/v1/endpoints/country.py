from typing import Annotated
from fastapi import APIRouter, Depends
from app.api.deps import get_country_service
from app.schemas.country import CountryCreate,CountryResponse,CountryUpdate
from app.services.country_service import CountryService


router = APIRouter()

CountryServiceDep = Annotated[CountryService,Depends(get_country_service)]

@router.post("/",response_model=CountryResponse,status_code=202)
def create_country(country: CountryCreate,service:CountryServiceDep):
    return service.create(country)


@router.get("/{id}",response_model = CountryResponse)
def get_id(id:int,service:CountryServiceDep):
    return service.get_by_id(id)

@router.put("/{id}",response_model=CountryResponse)
def update_by_id(id: int, country: CountryUpdate, service: CountryServiceDep):
    return service.update(id,country)


@router.delete("/{id}",response_model = CountryResponse)
def delete_by_id(id: int, service: CountryServiceDep):
    return service.delete(id)