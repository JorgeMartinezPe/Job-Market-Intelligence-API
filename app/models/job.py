from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, Float, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base
from sqlalchemy.orm import relationship
from app.models.associations import job_skills
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, index=True,nullable=False)
    description = Column(Text)
    salary_max= Column(Numeric)
    annual_salary = Column(Numeric)  # salario anual puntual (annual_salary_usd del dataset)
    salary_min = Column(Numeric)
    currency = Column(String)
    external_id = Column(String, unique=True, nullable=True)  # job_id del dataset (ej. AIJOB0001)
    job_category = Column(Text, index=True)
    experience_level = Column(Text, index=True)
    years_of_experience = Column(Integer)
    education_required = Column(Text)
    remote_work = Column(Text)  # On-site / Hybrid / Remote
    posting_year = Column(Integer, index=True)
    posting_month = Column(Integer)
    ai_salary_premium_pct = Column(Float)
    demand_score = Column(Float)
    demand_growth_yoy_pct = Column(Float)
    benefits_score = Column(Float)
    is_llm_role = Column(Boolean)
    published_at = Column(DateTime, server_default=func.now())
    location_id = Column(Integer,
        ForeignKey("location.id",ondelete="SET NULL"),
        nullable=True,
        index=True                    
    )
    company_id = Column( Integer,
        ForeignKey("company.id",ondelete="SET NULL"), #Evita que eliminando una compañia se borren los trabajos
        nullable=True,
        index=True                  
    )
    skills = relationship( #Tabla intermedia, ayuda a realizar los joins
        "Skill",
        secondary=job_skills,
        back_populates="jobs"
    )
    company = relationship("Company",back_populates="jobs")
    location = relationship("Location",back_populates="jobs")
