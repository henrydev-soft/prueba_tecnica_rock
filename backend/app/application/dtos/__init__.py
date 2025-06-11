"""
Paquete de Data Transfer Objects (DTOs)

Este paquete contiene los modelos Pydantic utilizados para la validación, serialización
y deserialización de datos en la comunicación entre la API (interfaces) y la capa de 
aplicación.

Los DTOs definen estructuras claras para:
- Entrada de datos (crear/actualizar entidades).
- Salida de datos (lectura y respuesta al cliente).

Cada módulo dentro del paquete corresponde a una entidad del dominio, e incluye
modelos específicos para los diferentes tipos de operación: creación, lectura,
actualización.

DTOs definidos:
- `course.py`: modelos relacionados con la entidad Course.
- `lesson.py`: modelos relacionados con la entidad Lesson.

Este enfoque ayuda a mantener una separación clara entre la lógica de negocio
(modelos de dominio), la infraestructura (ORM) y la presentación (API).

Autor: Henry Jiménez
Fecha: 2025-06-11
"""
from .course import CourseCreate, CourseUpdate, CourseRead, CourseWithLessons
from .lesson import LessonCreate, LessonUpdate, LessonRead

__all__ = [
    "CourseCreate", "CourseUpdate", "CourseRead", "CourseWithLessons",
    "LessonCreate", "LessonUpdate", "LessonRead"
]
