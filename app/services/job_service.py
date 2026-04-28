from sqlalchemy.orm import Session
from app.models.job import Job as JobModel
from app.schemas.job import Job as JobSchema, JobCreate

class JobService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_jobs(self):
        return self.db.query(JobModel).all()

    def create_job(self, job: JobCreate):
        db_job = JobModel(**job.dict())
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return db_job
    
