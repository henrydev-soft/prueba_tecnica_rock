"""
Modelos ORM de SQLAlchemy

Este subpaquete contiene los modelos de base de datos definidos mediante SQLAlchemy ORM,
correspondientes a las entidades del dominio. Estos modelos se encargan de mapear
las estructuras de datos de alto nivel (`Course`, `Lesson`) a tablas SQL reales.

Cada archivo representa un modelo de tabla, y está diseñado para ser usado dentro de la
infraestructura del sistema, desacoplado de la lógica de negocio o de entrada/salida.

Modelos definidos:
- `CourseModel`: tabla 'courses'
- `LessonModel`: tabla 'lessons'

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from .course_model import CourseModel
from .lesson_model import LessonModel

__all__ = ["CourseModel", "LessonModel"]
