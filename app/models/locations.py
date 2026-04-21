from sqlalchemy import Column, Integer,Text, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer,primary_key=True,index=True)
    country = Column(Text, nullable=False)
    state = Column(Text)
    city = Column(Text)

    jobs = relationship("Job",back_populates="location")