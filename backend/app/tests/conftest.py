"""
conftest.py

Fixtures globales para pruebas con Alembic y PostgreSQL de pruebas usando configuración desde `.env`.

Este archivo:
1. Carga configuración desde el archivo `.env` con get_settings().
2. Aplica migraciones con Alembic usando la base de datos de pruebas.
3. Ejecuta rollback automático después de cada prueba.
4. Sobrescribe la dependencia `get_db` para usar la sesión de pruebas.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

import os
import pytest
from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command
from app.core.logger import logger
from app.core.config import get_settings

# Cargar configuración desde .env
os.environ["PYTEST_CURRENT_TEST"] = "true"
settings = get_settings()

# Construir URL completa para la base de datos de prueba
TEST_DB_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.TEST_POSTGRES_DB}"
)

# Crear engine y sessionmaker para pruebas
engine_test = create_engine(TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Alembic: configuración de migraciones para entorno de test
@pytest.fixture(scope="session")
def alembic_config():
    config = Config("alembic.ini")
    config.set_main_option("sqlalchemy.url", TEST_DB_URL)
    return config

# Ejecutar migraciones antes de correr tests
@pytest.fixture(scope="session", autouse=True)
def setup_database_once(alembic_config):
    logger.info("⚙️ Aplicando migraciones de Alembic para entorno de pruebas...")
    command.upgrade(alembic_config, "head")
    logger.info("✅ Migraciones aplicadas.")

# Fixture de sesión de prueba (rollback automático por test)
@pytest.fixture(scope="function")
def db_session():
    connection = engine_test.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

# Cliente de pruebas con sesión de pruebas inyectada
@pytest.fixture(scope="function")
def client(db_session):
    from fastapi.testclient import TestClient
    from app.main import app
    from app.interfaces.http.api.v1.deps import get_db 

    def override_db():
        yield db_session

    app.dependency_overrides[get_db] = override_db

    return TestClient(app)