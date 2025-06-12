"""
Interfaces de repositorios del dominio

Este paquete contiene las interfaces (puertos de salida) que definen cómo debe accederse
a los datos de las entidades del dominio desde la perspectiva de la lógica de negocio.

Estas interfaces no contienen detalles técnicos de persistencia, y permiten
desacoplar los servicios de aplicación de cualquier implementación concreta (como una base de datos SQL).

Interfaces definidas:
- ICourseRepository: interfaz para operaciones sobre cursos.
- ILessonRepository: interfaz para operaciones sobre lecciones.

Sus implementaciones concretas se encuentran en `infrastructure/repositories/`.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from .course_repository import ICourseRepository
from .lesson_repository import ILessonRepository

__all__ = ["ICourseRepository", "ILessonRepository"]
