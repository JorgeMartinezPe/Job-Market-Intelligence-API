from fastapi import FastAPI, Depends, HTTPException
from app.api.v1.api import api_router
from sqlalchemy import text
from app.db.session import get_db
from sqlalchemy.orm import Session
app = FastAPI(
    title="Job Market Intelligence API",
    description="API for analyzing job market data",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    try:
        # Intenta una consulta simple
        db.execute(text("SELECT 1"))
        return {"status": "conectado", "mensaje": "Base de datos funcionando"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))