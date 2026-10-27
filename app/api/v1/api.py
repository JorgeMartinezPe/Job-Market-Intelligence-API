from fastapi import APIRouter

from app.api.v1.endpoints import company, health, jobs

api_router = APIRouter()
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(company.router, prefix="/companies", tags=["companies"])
api_router.include_router(health.router, tags=["health"])
