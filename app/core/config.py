from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Job Market Intelligence API"
    DATABASE_URL: str
    DESCRIPTION : str = "Analisis de datos de informacion y busqueda potenciada con IA"
    VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
