"""
Configuración de la sesión de base de datos

Este módulo configura el motor de SQLAlchemy y la clase de sesión local (`SessionLocal`)
para interactuar con la base de datos. El motor se crea utilizando los parámetros definidos
en la configuración de entorno.

Responsabilidades:
- Crear el motor de conexión a PostgreSQL.
- Exponer una clase `SessionLocal` para usar en dependencias de FastAPI.
- Integrarse con los modelos ORM a través del `Base` definido en `base.py`.

Este archivo forma parte de la infraestructura de persistencia del sistema.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

# Importar Base centralizada
from app.infrastructure.sql import Base  
from app.core import logger

settings = get_settings()

# Crear el motor de conexión (echo=True habilita logs de SQL para debug).
engine = create_engine(settings.DATABASE_URL, echo=True)
logger.info("Motor de base de datos SQLAlchemy creado correctamente.")

# Configurar la clase de sesión que se usará en dependencias de la app.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

