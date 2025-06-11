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
from app.infrastructure.repositories import LessonRepository
from app.infrastructure.repositories import CourseRepository
from app.application.services import LessonService
from app.application.dtos import LessonCreate, LessonUpdate, LessonRead

router = APIRouter(prefix="", tags=["Lessons"])


def get_lesson_service(db: Session = Depends(get_db)) -> LessonService:
    lesson_repo = LessonRepository(db)
    course_repo = CourseRepository(db)
    return LessonService(lesson_repo, course_repo)


@router.post("/courses/{course_id}/lessons/", response_model=LessonRead, status_code=status.HTTP_201_CREATED)
def create_lesson(course_id: int, data: LessonCreate, service: LessonService = Depends(get_lesson_service)):
    return service.create_lesson(course_id, data)


@router.put("/lessons/{lesson_id}", response_model=LessonRead)
def update_lesson(lesson_id: int, data: LessonUpdate, service: LessonService = Depends(get_lesson_service)):
    return service.update_lesson(lesson_id, data)


@router.delete("/lessons/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: int, service: LessonService = Depends(get_lesson_service)):
    service.delete_lesson(lesson_id)


@router.get("/lessons/{lesson_id}", response_model=LessonRead)
def get_lesson(lesson_id: int, service: LessonService = Depends(get_lesson_service)):
    return service.get_lesson(lesson_id)
