"""
En este archivo se define la clase con las variables de configuración de la aplicación. 
Utiliza pydantic para cargar los valores desde un archivo .env o desde variables de entorno.
"""

from pydantic_settings  import BaseSettings
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote_plus


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

    #Propiedad que construye la URL de conexión a PostgreSQL
    @property
    def DATABASE_URL(self) -> str:
        password_escaped = quote_plus(self.POSTGRES_PASSWORD)
        return(
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{password_escaped}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = Path(__file__).resolve().parents[3] / ".env"
        env_file_encoding = "utf-8"

#Función que agregar el cache de la instancia para evitar múltiples lecturas del archivo .env
@lru_cache
def get_settings() -> Settings:
    return Settings()