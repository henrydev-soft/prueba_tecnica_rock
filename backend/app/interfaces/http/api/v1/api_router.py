"""
Enrutador principal de la versión 1 de la API

Registra y organiza todos los subenrutadores definidos en el paquete `routes`,
exponiéndolos bajo el prefijo `/api/v1`. Esta capa representa la interfaz HTTP
de entrada hacia la lógica de aplicación.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from fastapi import APIRouter
from app.interfaces.http.api.v1.routes import course_router, lesson_router

router = APIRouter()
router.include_router(course_router)
router.include_router(lesson_router)
