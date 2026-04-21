from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, unique=True, nullable=False)

    jobs = relationship(
        "Job",
        secondary="job_skills",
        back_populates="skills"
    )