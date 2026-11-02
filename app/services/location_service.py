from typing import Optional

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
                Location(country=country, state=state, city=city)
            )
        return location
