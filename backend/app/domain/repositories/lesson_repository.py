"""
Interfaz de repositorio para la entidad Lesson

Define las operaciones CRUD esperadas por la capa de dominio.
Debe ser implementada por la infraestructura para desacoplar
la lógica de negocio del acceso a datos.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models import Lesson


class ILessonRepository(ABC):
    @abstractmethod
    def get_by_id(self, lesson_id: int) -> Optional[Lesson]:
        pass

    @abstractmethod
    def create(self, lesson: Lesson) -> Lesson:
        pass

    @abstractmethod
    def update(self, lesson: Lesson) -> Lesson:
        pass

    @abstractmethod
    def delete(self, lesson: Lesson) -> None:
        pass
