from app.core.exceptions import NotFoundError,ValidationError
from app.models.country import Country
from app.repositories.country_repository import CountryRepository
from app.schemas.country import CountryCreate,CountryUpdate
from sqlalchemy import select,or_
class CountryService:

    def __init__(self, repository: CountryRepository):
        self.repository = repository

    def create(self, data:CountryCreate)-> Country:
        new_country = Country(**data.model_dump())
        if self.repository.get_by_code_or_name(data.code,data.name):
            raise ValidationError("Ese pais ya existe")




        self.repository.add(new_country)
        self.repository.commit()
        self.repository.refresh(new_country)
        return new_country

        
    def get_by_id(self, country_id: int)-> Country:
        country = self.repository.get(country_id)
        if not country:
            raise NotFoundError("Country not found")
        return country

    def update(self, country_id: int, data: CountryUpdate)-> Country:
        country = self.get_by_id(country_id)
        if self.repository.get_by_code_or_name(data.code,data.name):
            raise ValidationError("Ese pais ya existe")

        for field,value in data.model_dump(exclude_unset=True).items():
            setattr(country,field,value)
        self.repository.commit()
        self.repository.refresh(country)
        return country
    


    def delete(self, country_id: int)-> Country:
        country = self.get_by_id(country_id)
        self.repository.delete(country)
        self.repository.commit()
        return country