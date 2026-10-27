"""Carga el dataset CSV en la base de datos.

Uso (desde la raiz del proyecto, con DATABASE_URL definida y migraciones aplicadas):
    python -m scripts.seed_csv
    python -m scripts.seed_csv --file data/raw/otro.csv

Es idempotente: los trabajos ya cargados (external_id = job_id del CSV) se omiten.
El dataset no trae nombre de empresa, asi que se crea una Company (name NULL) por cada
combinacion industry + company_size y los trabajos la comparten.
"""
import argparse
import csv
from datetime import datetime
from pathlib import Path

from sqlalchemy.orm import Session

import app.models  # noqa: F401
from app.db.session import get_engine
from app.models.companies_db import Company
from app.models.job import Job
from app.services.location_service import get_or_create_location
from app.services.skill_service import get_or_create_skills

DEFAULT_FILE = Path("data/raw/ai_jobs_market_2025_2026.csv")


def _num(value, cast=float):
    return cast(value) if value not in ("", None) else None


def get_or_create_company(db: Session, cache: dict, industry: str, size: str) -> Company:
    key = (industry, size)
    if key not in cache:
        company = (
            db.query(Company)
            .filter(Company.name.is_(None), Company.industry == industry, Company.size == size)
            .first()
        )
        if not company:
            company = Company(name=None, industry=industry, size=size)
            db.add(company)
            db.flush()
        cache[key] = company
    return cache[key]


def seed(path: Path) -> None:
    with Session(get_engine()) as db:
        existing = {row[0] for row in db.query(Job.external_id).filter(Job.external_id.isnot(None))}
        companies: dict = {}
        inserted = skipped = 0

        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row["job_id"] in existing:
                    skipped += 1
                    continue

                location = get_or_create_location(
                    db, country=row["country"], state=None, city=row["city"] or None
                )
                company = get_or_create_company(db, companies, row["industry"], row["company_size"])
                year, month = _num(row["posting_year"], int), _num(row["posting_month"], int)

                job = Job(
                    external_id=row["job_id"],
                    title=row["job_title"],
                    job_category=row["job_category"],
                    experience_level=row["experience_level"],
                    years_of_experience=_num(row["years_of_experience"], int),
                    education_required=row["education_required"],
                    annual_salary=_num(row["annual_salary_usd"]),
                    salary_min=_num(row["salary_min_usd"]),
                    salary_max=_num(row["salary_max_usd"]),
                    currency="USD",
                    remote_work=row["remote_work"],
                    posting_year=year,
                    posting_month=month,
                    published_at=datetime(year, month, 1) if year and month else None,
                    ai_salary_premium_pct=_num(row["ai_salary_premium_pct"]),
                    demand_score=_num(row["demand_score"]),
                    demand_growth_yoy_pct=_num(row["demand_growth_yoy_pct"]),
                    benefits_score=_num(row["benefits_score_10"]),
                    is_llm_role=row["is_llm_role"] == "1",
                    location_id=location.id,
                    company_id=company.id,
                )
                job.skills = get_or_create_skills(db, row["required_skills"].split("|"))
                db.add(job)
                inserted += 1

        db.commit()
    print(f"Insertados: {inserted} | Omitidos (ya existian): {skipped}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seeder del dataset de empleos")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE)
    seed(parser.parse_args().file)
