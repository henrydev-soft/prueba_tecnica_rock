"""
Rutas HTTP para la gestión de lecciones

Define los endpoints REST para crear, actualizar, eliminar y consultar
lecciones. Requiere un curso asociado para la creación.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.interfaces.http.api.v1.deps import get_db
from app.infrastructure.sql.repositories import SQLLessonRepository
from app.infrastructure.sql.repositories import SQLCourseRepository
from app.application.services import LessonService
from app.application.dtos import LessonCreate, LessonUpdate, LessonRead

router = APIRouter(prefix="/courses", tags=["Lessons"])


def get_lesson_service(db: Session = Depends(get_db)) -> LessonService:
    lesson_repository = SQLLessonRepository(db)
    course_repository = SQLCourseRepository(db)
    return LessonService(lesson_repository, course_repository)

@router.get("/{course_id}/lessons/{lesson_id}", response_model=LessonRead)
def get_lesson(lesson_id: int, service: LessonService = Depends(get_lesson_service)):
    """ Obtener una lección específica dentro de un curso """
    return service.get_lesson(lesson_id)


@router.post("/{course_id}/lessons/", response_model=LessonRead, status_code=status.HTTP_201_CREATED)
def create_lesson(course_id: int, data: LessonCreate, service: LessonService = Depends(get_lesson_service)):
    """ Crear una lección para un curso específico """
    return service.create_lesson(course_id, data)


@router.put("/{course_id}/lessons/{lesson_id}", response_model=LessonRead)
def update_lesson(lesson_id: int, data: LessonUpdate, service: LessonService = Depends(get_lesson_service)):
    """ Actualizar una lección específica dentro de un curso """
    return service.update_lesson(lesson_id, data)


@router.delete("/{course_id}/lessons/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: int, service: LessonService = Depends(get_lesson_service)):
    """ Eliminar una lección específica dentro de un curso """
    service.delete_lesson(lesson_id)
