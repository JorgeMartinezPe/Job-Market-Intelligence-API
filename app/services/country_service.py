from app.core.exceptions import NotFoundError, ValidationError
from app.models.country import Country
from app.repositories.country_repository import CountryRepository
from app.schemas.country import CountryCreate,CountryUpdate,CountryResponse


class CountryService:

    def __init__(self, repository: CountryCreate):
        self.repository = repository

    def create(self,data:CountryCreate)->Country:
        new_country = Country(**data.model_dump())
        self.repository.add(new_country)
        self.repository.commit()
        self.repository.refresh(new_country)
        return new_country
