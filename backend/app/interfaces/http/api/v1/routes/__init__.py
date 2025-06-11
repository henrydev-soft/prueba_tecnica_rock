"""
Rutas de la API versión 1

Este subpaquete agrupa las rutas organizadas por entidad (ej. cursos y lecciones)
y define los endpoints específicos para cada recurso.

Cada módulo contiene:
- Métodos HTTP REST (GET, POST, PUT, DELETE).
- Lógica mínima de enrutamiento.
- Inyección de dependencias que delegan a servicios de aplicación.

Archivos incluidos:
- `course.py`: CRUD de cursos.
- `lesson.py`: CRUD de lecciones por curso.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from .course import router as course_router
from .lesson import router as lesson_router

__all__ = ["course_router", "lesson_router"]