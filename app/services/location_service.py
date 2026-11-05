from typing import Optional
from app.core.exceptions import NotFoundError,ValidationError
from app.schemas.locations import LocationCreate
from app.models.locations import Location
from app.repositories.location_repository import LocationRepository


class LocationService:
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    def get_or_create(
        self, country: str, state: Optional[str], city: Optional[str]
    ) -> Location:
        country = country.strip().lower()
        state = state.strip().lower() if state else None
        city = city.strip().lower() if city else None

        location = self.repository.find_by_fields(country, state, city)
        if not location:
            location = self.repository.add(
                Location(country=country, state=state, city = city)
            )
        return location
    
    def get_location_by_id(self, location_id:int)-> Location:
            location = self.repository.get(location_id)
            if not location:
                raise NotFoundError("No existe esta location")
            
    def update(self,location_id: int,data:LocationCreate) ->Location:
        location = self.get_location_by_id(location_id)
        if self.repository.get_by_code_and_name(data.country,data.city,data.state):
             ValidationError("Esta location ya existe...")

   

    def delete_location(self,location_id:int)-> Location:
        location = self.get_location_by_id(location_id)
        self.repository.delete(location)
        self.repository.commit()
        return location

