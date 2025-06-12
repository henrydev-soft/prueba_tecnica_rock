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


def get_env_file_path() -> Optional[Path]:
    """
    Retorna la ruta del archivo .env si no se está en Docker.
    Si se detecta que estamos dentro de Docker (por una variable), retorna None.
    """
    if os.getenv("RUNNING_IN_DOCKER") == "true":
        return None  # No cargar archivo .env
    # En local: buscar el .env en la raíz del proyecto
    return Path(__file__).resolve().parents[3] / ".env"

env_path = get_env_file_path()

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

        
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{db_name}"
        )

    model_config = ConfigDict(
        env_file=str(env_path) if env_path and env_path.exists() else None,
        env_file_encoding="utf-8"
    )

#Función que agregar el cache de la instancia para evitar múltiples lecturas del archivo .env
@lru_cache
def get_settings() -> Settings:
    return Settings()