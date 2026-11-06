from typing import Annotated
from fastapi import APIRouter, Depends
from app.api.deps import LocationService, get_location_service
from app.schemas.locations import LocationCreate, LocationResponse, LocationUpdate

router = APIRouter()

LocationServiceDep = Annotated[LocationService, Depends(get_location_service)]

@router.post("/",response_model = LocationResponse, status_code=200)
def create_company(location: LocationCreate,service: LocationServiceDep):
    return service.create_location(location)

@router.put("{id}",response_model = LocationResponse, status_code = 200 )
def update_location(location:LocationUpdate, service: LocationServiceDep):
    return service.update(location)

@router.get("/{id}", response_model=LocationResponse, status_code=202)
def get_one(id: int, service:LocationServiceDep):
    return service.get_location_by_id(id)