from sqlalchemy.orm import Session
from app.models.country import Country
from app.repositories.base_repository import BaseRepository
from sqlalchemy import select,or_
from typing import Optional
class CountryRepository(BaseRepository[Country]):
    def __init__(self, db:Session):
        super().__init__(db,Country)


    def get_by_code_or_name(self,code,name:str) -> Optional[Country]:
        return(
            self.db.query(Country)
            .filter(or_(Country.code == code, Country.name == name))
            .first()
        )