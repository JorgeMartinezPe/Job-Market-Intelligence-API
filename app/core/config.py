import os

from dotenv import load_dotenv

load_dotenv()  # cargar variables de entorno desde .env


class Settings:
    PROJECT_NAME: str = "Job Market Intelligence API"
    DESCRIPTION: str = "API for analyzing job market data"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"

    @property
    def database_url(self) -> str:
        # Se valida al usarla (no al importar) para poder importar la app en tests sin BD
        url = os.getenv("DATABASE_URL")
        if not url:
            raise ValueError("DATABASE_URL no está definida")
        return url


settings = Settings()
