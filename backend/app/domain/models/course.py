"""
Course Entity

Este módulo define la entidad de dominio `Course`, la cual representa un curso virtual
dentro del sistema. Un curso tiene un identificador, título, descripción, un nombre de
instructor y una lista de lecciones asociadas.

Esta entidad es utilizada en la capa de dominio y no depende de frameworks externos
como ORMs o librerías de serialización.

Responsabilidades:
- Encapsular la estructura de datos de un curso.
- Actuar como modelo base en los servicios de aplicación y repositorios.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from dataclasses import dataclass, field
from typing import List, Optional
from .lesson import Lesson

@dataclass
class Course:
    title:str
    description: str
    instructor: str
    lessons: Optional[List[Lesson]] = field(default_factory=list)
    id: Optional[int] = None