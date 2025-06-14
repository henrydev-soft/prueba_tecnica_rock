"""
Servicio de aplicación para la entidad Course

Este módulo define la clase `CourseService`, encargada de ejecutar la lógica
de negocio relacionada con los cursos. Usa un repositorio inyectado para acceder
a la persistencia, y lanza excepciones de dominio que serán gestionadas
por los manejadores globales.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from app.domain.repositories import ICourseRepository
from app.application.dtos.course import CourseCreate, CourseUpdate
from app.domain.models.course import Course
from app.core.logger import logger
from app.core.exceptions import CourseNotFound


class CourseService:
    def __init__(self, repository: ICourseRepository):
        self.repository: ICourseRepository = repository

    def list_courses(self) -> list[Course]:
        logger.info("Listando todos los cursos")
        return self.repository.get_all()

    def get_course(self, course_id: int) -> Course:
        logger.info("Buscando curso con ID=%s", course_id)
        course = self.repository.get_by_id(course_id)
        if not course:
            logger.warning("Curso con ID=%s no encontrado", course_id)
            raise CourseNotFound(course_id)
        return course

    def create_course(self, data: CourseCreate) -> Course:
        logger.info("Creando curso con título: '%s'", data.title)
        new_course = Course(**data.model_dump())
        created = self.repository.create(new_course)
        logger.info("Curso creado exitosamente con ID=%s", created.id)
        return created

    def update_course(self, course_id: int, data: CourseUpdate) -> Course:
        logger.info("Actualizando curso con ID=%s", course_id)
        course = self.get_course(course_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(course, field, value)
        updated = self.repository.update(course)
        logger.info("Curso con ID=%s actualizado", course_id)
        return updated

    def delete_course(self, course_id: int) -> None:
        logger.info("Eliminando curso con ID=%s", course_id)
        course = self.get_course(course_id)
        self.repository.delete(course)
        logger.info("Curso con ID=%s eliminado correctamente", course_id)
