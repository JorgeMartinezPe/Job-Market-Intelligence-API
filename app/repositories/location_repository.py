from typing import Optional

from sqlalchemy.orm import Session

from app.models.locations import Location
from app.repositories.base_repository import BaseRepository
from sqlalchemy import select,or_,and_

class LocationRepository(BaseRepository[Location]):
    def __init__(self, db: Session):
        super().__init__(db, Location)

    def find_by_fields(
        self, country: str, state: Optional[str], city: Optional[str]
    ) -> Optional[Location]:
        return (
            self.db.query(Location)
            .filter_by(country=country, state=state, city=city)
            .first()
        )

    def get_by_code_and_name(self, country:str, city: str,state:str)-> Optional[Location]:
        return(
            self.db.query(Location)
            .filter(and_(Location.country == country,Location.city == city,Location.state ==state))
            .first()
        )
    
