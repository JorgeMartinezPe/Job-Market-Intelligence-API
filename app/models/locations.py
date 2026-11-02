from sqlalchemy import Column, Integer, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.session import Base


class Location(Base):
    __tablename__ = "location"
    __table_args__ = (
        # nulls_not_distinct: (pais, NULL, NULL) tambien cuenta como duplicado (PostgreSQL 15+)
        UniqueConstraint("country", "state", "city", name="uq_location_country_state_city",
                         postgresql_nulls_not_distinct=True),
    )
    id = Column(Integer,primary_key=True,index=True)
    country = Column(Text, nullable=False)
    state = Column(Text)
    city = Column(Text)

    jobs = relationship("Job",back_populates="location")