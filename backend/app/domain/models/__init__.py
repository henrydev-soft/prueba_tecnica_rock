"""
Paquete de modelos del dominio

Este paquete contiene las entidades centrales del dominio de la aplicación, como `Course` y `Lesson`.
Estas clases representan conceptos del negocio de forma pura, sin depender de frameworks externos
como ORMs, APIs o serializadores.

Los modelos del dominio son utilizados por los servicios de aplicación y repositorios como
fuente de verdad para las reglas de negocio, garantizando una separación clara respecto
a la infraestructura y a la capa de presentación.

Entidades definidas:
- Course: representa un curso virtual.
- Lesson: representa una lección vinculada a un curso.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from .course import Course
from .lesson import Lesson

__all__ = ["Course", "Lesson"]
