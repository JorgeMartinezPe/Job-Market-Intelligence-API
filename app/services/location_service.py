from typing import Optional
from app.core.exceptions import NotFoundError,ValidationError
from app.schemas.locations import LocationCreate
from app.models.locations import Location
from app.repositories.location_repository import LocationRepository


class LocationService:
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    def create_location (self, data:LocationCreate)-> Location:
         new_location = Location(**data.model_dump())
         if self.repository.get_by_code_and_name(data.country,data.city,data.state):
              raise ValidationError("Esa locación ya existe")


         self.repository.add(new_location)
         self.repository.commit()
         self.repository.refresh(new_location)
         return new_location
    
    def get_location_by_id(self, location_id:int)-> Location:
            location = self.repository.get(location_id)
            if not location:
                raise NotFoundError("No existe esta location")
            return location
            
    def update(self,location_id: int,data:LocationCreate) ->Location:
        location = self.get_location_by_id(location_id)
        if self.repository.get_by_code_and_name(data.country,data.city,data.state):
             ValidationError("Esta location ya existe...")

        return location

   

    def delete_location(self,location_id:int)-> Location:
        location = self.get_location_by_id(location_id)
        self.repository.delete(location)
        self.repository.commit(location)
        return location

