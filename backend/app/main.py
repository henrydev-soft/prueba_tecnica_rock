"""
Punto de entrada principal de la aplicación FastAPI

Este archivo inicializa la instancia de la aplicación, configura middlewares
y registra las rutas de la API.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import settings, logger
from app.interfaces.http.api.v1 import api_v1_router
from app.core.exception_handlers import register_exception_handlers


def create_application() -> FastAPI:
    logger.info("Iniciando aplicación...")

    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="1.0.0"
    )

    # Configuración de CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Cambiar esto en producción
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Registro de rutas
    app.include_router(api_v1_router, prefix="/api/v1")

    #Registar controlador de excepciones global
    register_exception_handlers(app)

    logger.info(f"{settings.APP_NAME} cargada con éxito.")
    return app


app = create_application()
