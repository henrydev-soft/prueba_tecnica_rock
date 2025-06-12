"""
Implementaciones concretas de repositorios

Este paquete contiene la implementación concreta de los repositorios definidos
en el dominio, usando SQLAlchemy para realizar operaciones sobre una base de datos
relacional. Cada repositorio se encarga de mapear entidades de dominio
a modelos ORM y viceversa.

Implementaciones incluidas:
- `course_repository_sql.py`: acceso a datos para cursos.
- `lesson_repository_sql.py`: acceso a datos para lecciones.

Estas clases son inyectadas en los servicios de aplicación mediante dependencias.

Autor: [Tu Nombre]
Fecha: 2025-06-11
"""

from .course_repository_sql import SQLCourseRepository
from .lesson_repository_sql import SQLLessonRepository

__all__ = ["SQLCourseRepository", "SQLLessonRepository"]