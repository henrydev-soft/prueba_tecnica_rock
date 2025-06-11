"""
En este archivo se define la clase con las variables de configuración de la aplicación. 
Utiliza pydantic para cargar los valores desde un archivo .env o desde variables de entorno.
"""

import os
from pydantic_settings  import BaseSettings
from pydantic import ConfigDict
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote_plus
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "Course Manager"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    #Parámetros de conexión con la base de datos
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    TEST_POSTGRES_DB: Optional[str] = None

    #Propiedad que construye la URL de conexión a PostgreSQL
    @property
    def DATABASE_URL(self) -> str:
        db_name = self.POSTGRES_DB
        if os.getenv("PYTEST_CURRENT_TEST"):
            db_name = os.getenv("TEST_POSTGRES_DB", self.POSTGRES_DB + "_test")

        password_escaped = quote_plus(self.POSTGRES_PASSWORD)
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{password_escaped}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{db_name}"
        )

    model_config = ConfigDict(
            env_file=Path(__file__).resolve().parents[3] / ".env",
            env_file_encoding="utf-8"
        )

#Función que agregar el cache de la instancia para evitar múltiples lecturas del archivo .env
@lru_cache
def get_settings() -> Settings:
    return Settings()