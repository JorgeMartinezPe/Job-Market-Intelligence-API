from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    salary = Column(String)
    skills = Column(String)  # Could be JSON or comma-separated
    created_at = Column(DateTime(timezone=True), server_default=func.now())