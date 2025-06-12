"""
Implementación del repositorio de lecciones con SQLAlchemy

Este módulo implementa la interfaz ILessonRepository utilizando SQLAlchemy
para realizar operaciones de persistencia sobre la entidad Lesson.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from sqlalchemy.orm import Session
from app.domain.models import Lesson
from app.domain.repositories import ILessonRepository
from app.infrastructure.sql.models import LessonModel
from typing import Optional


class SQLLessonRepository(ILessonRepository):
    
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, lesson_id: int) -> Optional[Lesson]:
        lesson_model = self.db.query(LessonModel).filter(LessonModel.id == lesson_id).first()
        return self._to_domain(lesson_model) if lesson_model else None

    def create(self, lesson: Lesson) -> Lesson:
        lesson_model = self._from_domain(lesson)
        self.db.add(lesson_model)
        self.db.commit()
        self.db.refresh(lesson_model)
        return self._to_domain(lesson_model)

    def update(self, lesson: Lesson) -> Lesson:
        lesson_model = self.db.query(LessonModel).filter(LessonModel.id == lesson.id).first()
        if not lesson_model:
            return None
        lesson_model.title = lesson.title
        lesson_model.video_url = lesson.video_url
        lesson_model.course_id = lesson.course_id
        self.db.commit()
        self.db.refresh(lesson_model)
        return self._to_domain(lesson_model)

    def delete(self, lesson: Lesson) -> None:
        lesson_model = self.db.query(LessonModel).filter(LessonModel.id == lesson.id).first()
        if lesson_model:
            self.db.delete(lesson_model)
            self.db.commit()

    def _to_domain(self, model: LessonModel) -> Lesson:
        return Lesson(
            id=model.id,
            title=model.title,
            video_url=model.video_url,
            course_id=model.course_id
        )

    def _from_domain(self, lesson: Lesson) -> LessonModel:
        return LessonModel(
            id=lesson.id,
            title=lesson.title,
            video_url=lesson.video_url,
            course_id=lesson.course_id
        )