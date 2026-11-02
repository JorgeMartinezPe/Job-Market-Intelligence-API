from functools import lru_cache

from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker( #crear la sesion y pasarle todos los datos
    autocommit=False,
    autoflush=False,
    bind=engine
)
=======
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings
>>>>>>> eccfe6b12233fb220f13d162ecbea7c7868cc263

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
