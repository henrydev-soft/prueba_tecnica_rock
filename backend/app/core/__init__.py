"""
Paquete central de configuración y utilidades

Este paquete agrupa los componentes fundamentales y reutilizables de la aplicación,
como la configuración global (`settings`), el sistema de logs (`logger`), 
el manejo de excepciones personalizadas y herramientas de seguridad.

Módulos incluidos:
- `config`: configuración basada en variables de entorno.
- `logger`: sistema de logging centralizado.
- `exceptions`: definiciones de errores personalizados.
- `security`: funciones auxiliares de autenticación o hash.

Este paquete puede ser importado como núcleo de soporte de toda la arquitectura.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from .config import get_settings
from .logger import logger
from .exceptions import AppException
#from .security import verify_password, hash_password

# Instancia única de settings para uso global
settings = get_settings()

__all__ = [
    "settings",
    "logger",
    "AppException",
    "verify_password",
    "hash_password"
]
