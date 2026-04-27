from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import List
from app.schemas.companies import CompanyCreate,CompanyResponse,CompanyUpdate
from app.models.companies_db import Company
router = APIRouter()

#Create
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

#Select
@router.get("/obtain_company",response_model=List[CompanyResponse])
def obten_company(id:int,db:Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id ==id).all()
    return company
#Update
@router.put("/update_company/{id}")
def update_company(id:int,company:CompanyUpdate,db:Session = Depends(get_db)):
    company_db = db.query(Company).filter(Company.id == id).first() #Obtener de la base de datos
    if company_db is None: #Validar que existe
        return {"message": "Company not found"}
    
    company_db.name = company.name #Campos que se requeiren modificar, en el schema son opcionales.
    company_db.industry = company.industry
    company_db.size = company.size
    company_db.website = company.website
    
    db.commit()
    db.refresh(company_db)
    
    return {"message": "Company updated successfully", "company": company_db}

#delete
@router.delete("/delete_company){id}")
def delete_company(id:int,db:Session=Depends(get_db)):

    company_db = db.query(Company).filter(Company.id == id).first()
    if company_db is None:
        return {"message": "Company not found"}
    db.delete(company_db)
    db.commit()
    return {"Message":"Company has been deleting successfully","comapny":company_db}