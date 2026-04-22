from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import List
from app.schemas.companies import CompanyCreate,CompanyResponse
from app.models.companies_db import Company
router = APIRouter()

@router.post("/companies")
def create_company(company:CompanyCreate,db:Session = Depends(get_db)):
    new_company = Company(
        name=company.name,
        industry=company.industry, # De esta manera mediante el input del usuario se hace la insercion.
        size=company.size,
        website=company.website
    )
    
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return company

@router.get("/obtain_company",response_model=List[CompanyResponse])
def obten_company(id:int,db:Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id ==id).all()
    return company
