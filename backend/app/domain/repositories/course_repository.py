"""
Interfaz del repositorio de cursos

Define los métodos necesarios para gestionar la persistencia de objetos tipo `Course`.
Esta interfaz debe ser implementada por una clase concreta (por ejemplo, usando SQLAlchemy).

Permite desacoplar la lógica de aplicación del mecanismo específico de almacenamiento
siguiendo los principios de inversión de dependencias y arquitectura hexagonal.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from abc import ABC, abstractmethod
from typing import List
from app.domain.models import Course


class ICourseRepository(ABC):
    """
    Contrato que deben implementar todos los repositorios de cursos.
    """

    @abstractmethod
    def get_all(self) -> List[Course]:
        """Devuelve todos los cursos existentes."""
        pass

    @abstractmethod
    def get_by_id(self, course_id: int) -> Course | None:
        """Devuelve un curso por ID o None si no existe."""
        pass

    @abstractmethod
    def create(self, course: Course) -> Course:
        """Guarda un nuevo curso en la base de datos."""
        pass

    @abstractmethod
    def update(self, course: Course) -> Course:
        """Actualiza un curso existente."""
        pass

    @abstractmethod
    def delete(self, course: Course) -> None:
        """Elimina un curso existente."""
        pass
