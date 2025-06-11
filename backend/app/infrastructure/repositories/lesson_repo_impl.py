"""
Implementación del repositorio de lecciones con SQLAlchemy

Este módulo implementa la interfaz ILessonRepository utilizando SQLAlchemy
para realizar operaciones de persistencia sobre la entidad Lesson.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from sqlalchemy.orm import Session
from app.infrastructure.db.models.lesson_model import LessonModel
from app.domain.repositories.lesson_repo import ILessonRepository
from typing import Optional


class LessonRepository(ILessonRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, lesson_id: int) -> Optional[LessonModel]:
        return self.db.query(LessonModel).filter(LessonModel.id == lesson_id).first()

    def create(self, lesson: LessonModel) -> LessonModel:
        self.db.add(lesson)
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def update(self, lesson: LessonModel) -> LessonModel:
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def delete(self, lesson: LessonModel) -> None:
        self.db.delete(lesson)
        self.db.commit()
