from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker( #crear la sesion y pasarle todos los datos
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False)


@lru_cache
def get_engine():
    return create_engine(settings.DATABASE_URL)


def get_db():
    db = SessionLocal(bind=get_engine())
    try:
        yield db
    finally:
        db.close()
