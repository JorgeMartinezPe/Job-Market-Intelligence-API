from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()


@router.get("/ping-db")
def ping_db(db: Annotated[Session, Depends(get_db)]):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "conectado", "mensaje": "Base de datos funcionando"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
