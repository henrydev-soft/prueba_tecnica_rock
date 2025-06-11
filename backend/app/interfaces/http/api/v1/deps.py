"""
Dependencias comunes para la API

Este archivo contiene funciones de dependencia para FastAPI, incluyendo
la gestión del ciclo de vida de la sesión de base de datos.

Autor: Henry Jimenez
Fecha: 2025-06-11
"""

from typing import Generator
from app.infrastructure.db.session import SessionLocal


def get_db() -> Generator:
    """
    Proporciona una sesión de base de datos por solicitud.
    Se asegura de cerrar la sesión al finalizar el uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
