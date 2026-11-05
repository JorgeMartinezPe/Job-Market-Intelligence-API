from app.core.exceptions import NotFoundError, ValidationError
from app.models.companies_db import Company
from app.repositories.company_repository import CompanyRepository
from app.schemas.companies import CompanyCreate, CompanyUpdate
from sqlalchemy import select

class CompanyService:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    def create(self, data: CompanyCreate) -> Company:
        new_company = Company(**data.model_dump())

        
        
        self.repository.add(new_company)
        self.repository.commit()
        self.repository.refresh(new_company)
        return new_company


    def get_by_id(self, company_id: int) -> Company:
        company = self.repository.get(company_id)
        if not company:
            raise NotFoundError("Company not found")
        return company

    def update(self, company_id: int, data: CompanyUpdate) -> Company:
        company = self.get_by_id(company_id)

        # exclude_unset: solo toca los campos que el cliente envió,
        # en vez de sobrescribir todo con None (bug del código original).
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(company, field, value)

        self.repository.commit()
        self.repository.refresh(company)
        return company

    def delete(self, company_id: int) -> Company:
        company = self.get_by_id(company_id)
        self.repository.delete(company)
        self.repository.commit()
        return company
