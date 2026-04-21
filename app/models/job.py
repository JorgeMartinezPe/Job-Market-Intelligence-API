from sqlalchemy import Column, Integer, String, Text, DateTime,Numeric,ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base
from sqlalchemy.orm import relationship
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, index=True,nullable=False)
    description = Column(Text)
    salary_max= Column(Numeric)
    salary_min = Column(Numeric)
    published= Column(DateTime(timezone=True), server_default=func.now())
    location_id = Column(Integer,
        ForeignKey("location.id",ondelete="SET NULL"),
        nullable=True,
        index=True                    
    )
    company_id = Column( Integer,
        ForeignKey("company.id",ondelete="SET NULL"),
        nullable=True,
        index=True                  
    )
    skills = relationship(
        "Skill",
        secondary="job_skills",
        back_populates="jobs"
    )
    company = relationship("Company",back_populates="jobs")
    location = relationship("Location",back_populates="jobs")
