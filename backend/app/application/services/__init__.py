"""
Servicios de aplicación

Este paquete contiene los servicios encargados de la lógica de aplicación
(casos de uso), que se ubican entre la capa de interfaces (controladores/API)
y la capa de dominio (modelos y repositorios).

Responsabilidades:
- Coordinar operaciones del dominio.
- Orquestar validaciones de negocio.
- Transformar o adaptar datos entre capas.

Servicios incluidos:
- `course_service.py`: operaciones sobre cursos.
- `lesson_service.py`: operaciones sobre lecciones.

Autor: [Tu Nombre]
Fecha: 2025-06-11
"""

from .course_service import CourseService
from .lesson_service import LessonService

__all__ = ["CourseService", "LessonService"]
