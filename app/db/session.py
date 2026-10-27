from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False)


@lru_cache
def get_engine():
    return create_engine(settings.database_url)


def get_db():
    db = SessionLocal(bind=get_engine())
    try:
        yield db
    finally:
        db.close()
