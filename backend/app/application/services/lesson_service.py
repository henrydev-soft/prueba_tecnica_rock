"""
Servicio de aplicación para la entidad Lesson

Este servicio implementa la lógica de negocio para gestionar lecciones
asociadas a cursos. Maneja operaciones de creación, actualización, consulta
y eliminación, con validaciones de dominio y control de errores.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from app.domain.repositories import ILessonRepository
from app.domain.repositories import ICourseRepository
from app.application.dtos.lesson import LessonCreate, LessonUpdate
from app.infrastructure.db.models import LessonModel
from app.core.exceptions import LessonNotFound, CourseNotFound
from app.core.logger import logger


class LessonService:
    def __init__(self, lesson_repo: ILessonRepository, course_repo: ICourseRepository):
        self.lesson_repo = lesson_repo
        self.course_repo = course_repo

    def create_lesson(self, course_id: int, data: LessonCreate) -> LessonModel:
        logger.info("Creando lección para curso ID=%s", course_id)
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise CourseNotFound(course_id)

        new_lesson = LessonModel(**data.model_dump(), course_id=course_id)
        created = self.lesson_repo.create(new_lesson)
        logger.info("Lección creada con ID=%s", created.id)
        return created

    def update_lesson(self, lesson_id: int, data: LessonUpdate) -> LessonModel:
        logger.info("Actualizando lección ID=%s", lesson_id)
        lesson = self.lesson_repo.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFound(lesson_id)

        for field, value in data.dict(exclude_unset=True).items():
            setattr(lesson, field, value)

        updated = self.lesson_repo.update(lesson)
        logger.info("Lección actualizada con ID=%s", lesson_id)
        return updated

    def delete_lesson(self, lesson_id: int) -> None:
        logger.info("Eliminando lección ID=%s", lesson_id)
        lesson = self.lesson_repo.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFound(lesson_id)

        self.lesson_repo.delete(lesson)
        logger.info("Lección eliminada con ID=%s", lesson_id)

    def get_lesson(self, lesson_id: int) -> LessonModel:
        logger.info("Consultando lección ID=%s", lesson_id)
        lesson = self.lesson_repo.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFound(lesson_id)
        return lesson
