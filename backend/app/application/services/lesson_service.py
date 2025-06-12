"""
Servicio de aplicación para la entidad Lesson

Este servicio implementa la lógica de negocio para gestionar lecciones
asociadas a cursos. Maneja operaciones de creación, actualización, consulta
y eliminación, con validaciones de dominio y control de errores.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from app.domain.models.lesson import Lesson
from app.domain.repositories import ILessonRepository, ICourseRepository
from app.application.dtos.lesson import LessonCreate, LessonUpdate
from app.core.exceptions import LessonNotFound, CourseNotFound
from app.core.logger import logger


class LessonService:
    def __init__(self, lesson_repository: ILessonRepository, course_repository: ICourseRepository):
        self.lesson_repository = lesson_repository
        self.course_repository = course_repository

    def create_lesson(self, course_id: int, data: LessonCreate) -> Lesson:
        logger.info("Creando lección para curso ID=%s", course_id)
        course = self.course_repository.get_by_id(course_id)
        if not course:
            raise CourseNotFound(course_id)

        new_lesson = Lesson(
            id=None,  # Será asignado por la base de datos
            title=data.title,
            video_url=data.video_url,
            course_id=course_id
        )

        created = self.lesson_repository.create(new_lesson)
        logger.info("Lección creada con ID=%s", created.id)
        return created

    def update_lesson(self, lesson_id: int, data: LessonUpdate) -> Lesson:
        logger.info("Actualizando lección ID=%s", lesson_id)
        lesson = self.lesson_repository.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFound(lesson_id)

        updated_lesson = Lesson(
            id=lesson.id,
            title=data.title or lesson.title,
            video_url=data.video_url or lesson.video_url,
            course_id=lesson.course_id
        )

        updated = self.lesson_repository.update(updated_lesson)
        logger.info("Lección actualizada con ID=%s", updated.id)
        return updated

    def delete_lesson(self, lesson_id: int) -> None:
        logger.info("Eliminando lección ID=%s", lesson_id)
        lesson = self.lesson_repository.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFound(lesson_id)

        self.lesson_repository.delete(lesson)
        logger.info("Lección eliminada con ID=%s", lesson_id)

    def get_lesson(self, lesson_id: int) -> Lesson:
        logger.info("Consultando lección ID=%s", lesson_id)
        lesson = self.lesson_repository.get_by_id(lesson_id)
        if not lesson:
            raise LessonNotFound(lesson_id)
        return lesson
