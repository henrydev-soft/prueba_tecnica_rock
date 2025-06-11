"""
Módulo de infraestructura de base de datos

Este paquete agrupa todos los componentes relacionados con la configuración y
uso de la base de datos dentro de la capa de infraestructura. Aquí se incluyen:

- `session.py`: configuración del motor y sesión SQLAlchemy.
- `base.py`: clase base declarativa compartida por los modelos ORM.
- `models/`: definición de los modelos de datos (ORM).
- `__init__.py`: punto de entrada para exponer modelos si se requiere (por ejemplo, para Alembic).

Este paquete es utilizado por los adaptadores secundarios para implementar
la persistencia de datos, siguiendo los principios de arquitectura hexagonal.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

# Este archivo puede usarse para importar los modelos y exponerlos a Alembic
from .base import Base
from .models.course_model import CourseModel
from .models.lesson_model import LessonModel

__all__ = ["Base", "CourseModel", "LessonModel"]
