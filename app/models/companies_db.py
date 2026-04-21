from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(Text, nullable=False)
    industry = Column(Text)
    size = Column(Text)
    website = Column(Text)
    jobs = relationship("Job",back_populates="company")