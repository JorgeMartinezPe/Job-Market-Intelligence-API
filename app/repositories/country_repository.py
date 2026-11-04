from sqlalchemy.orm import Session
from models.country import Country
from app.repositories.base_repository import BaseRepository

class CountryRepository(BaseRepository[Country]):
    def __init__(self, db:Session):
        super().__init__(db,Country)