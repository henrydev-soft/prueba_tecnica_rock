"""
Modelos ORM (SQLAlchemy)

Este paquete define los modelos de base de datos relacional utilizando SQLAlchemy.
Estos modelos son utilizados por los repositorios para mapear entidades de dominio
a estructuras físicas en una base de datos SQL.

Modelos definidos:
- `CourseModel`: tabla 'courses'
- `LessonModel`: tabla 'lessons'

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from .course_model import CourseModel
from .lesson_model import LessonModel

__all__ = ["CourseModel", "LessonModel"]
