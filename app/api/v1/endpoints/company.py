from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import Annotated
from app.schemas.companies import CompanyCreate, CompanyResponse, CompanyUpdate
from app.models.companies_db import Company

router = APIRouter()


# Create
@router.post("", response_model=CompanyResponse, status_code=201)
def create_company(company: CompanyCreate, db: Annotated[Session, Depends(get_db)]):
    new_company = Company(**company.model_dump())

    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company


# Select
@router.get("/obtain_company", response_model=CompanyResponse)
def obten_company(id: int, db: Annotated[Session, Depends(get_db)]):
    company = db.query(Company).filter(Company.id == id).first()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


# Update
@router.put("/update_company/{id}", response_model=CompanyResponse)
def update_company(id: int, company: CompanyUpdate, db: Annotated[Session, Depends(get_db)]):
    company_db = db.query(Company).filter(Company.id == id).first()
    if company_db is None:
        raise HTTPException(status_code=404, detail="Company not found")

    # Solo se modifican los campos enviados por el usuario
    for field, value in company.model_dump(exclude_unset=True).items():
        setattr(company_db, field, value)

    db.commit()
    db.refresh(company_db)
    return company_db


# Delete
@router.delete("/delete_company/{id}")
def delete_company(id: int, db: Annotated[Session, Depends(get_db)]):
    company_db = db.query(Company).filter(Company.id == id).first()
    if company_db is None:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(company_db)
    db.commit()
    return {"message": "Company deleted successfully"}
