"""
Implementaciones concretas de repositorios

Este paquete contiene las clases que implementan las interfaces de repositorio
definidas en la capa de dominio. Estas implementaciones utilizan SQLAlchemy
para realizar operaciones CRUD contra la base de datos.

Implementaciones incluidas:
- `course_repo_impl.py`: acceso a datos para cursos.
- `lesson_repo_impl.py`: acceso a datos para lecciones.

Estas clases son inyectadas en los servicios de aplicación mediante dependencias.

Autor: [Tu Nombre]
Fecha: 2025-06-11
"""

from .course_repo_impl import CourseRepository
from .lesson_repo_impl import LessonRepository

__all__ = ["CourseRepository", "LessonRepository"]
