"""
Adaptador SQL para infraestructura

Este paquete contiene la implementación específica de persistencia basada en
bases de datos relacionales (SQL), incluyendo configuración de sesiones,
modelos ORM y repositorios compatibles con tecnologías como PostgreSQL o MySQL.

Representa un adaptador tecnológico conectado a los puertos definidos en el dominio.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""


# Este archivo puede usarse para importar los modelos y exponerlos a Alembic
from .base import Base
from .session import SessionLocal
from .models.course_model import CourseModel
from .models.lesson_model import LessonModel

__all__ = ["Base", "SessionLocal,","CourseModel", "LessonModel"]
