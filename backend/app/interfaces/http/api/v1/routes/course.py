"""
Rutas HTTP para la gestión de cursos.

Incluye endpoints para:
- Listar todos los cursos
- Consultar un curso por ID
- Crear un nuevo curso
- Actualizar un curso existente
- Eliminar un curso

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.application.dtos.course import CourseRead, CourseCreate, CourseUpdate, CourseWithLessons
from app.interfaces.http.api.v1.deps import get_db
from app.infrastructure.sql.repositories import SQLCourseRepository
from app.application.services import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_course_service(db: Session = Depends(get_db)) -> CourseService:
    repo = SQLCourseRepository(db)
    return CourseService(repo)

@router.get("/", response_model=List[CourseRead])
def list_courses(service: CourseService = Depends(get_course_service)):
    """Listar todos los cursos"""
    return service.list_courses()

@router.get("/{course_id}", response_model=CourseWithLessons)
def get_course(course_id: int, service: CourseService = Depends(get_course_service)):
    """Obtener los datos de un curso por su id, incluye lista de lecciones asociadas"""
    return service.get_course(course_id)

@router.post("/", response_model=CourseRead, status_code=201)
def create_course(data: CourseCreate, service: CourseService = Depends(get_course_service)):
    """Crear un curso nuevo, no admite las lecciones en la misma petición"""
    return service.create_course(data)

@router.put("/{course_id}", response_model=CourseRead)
def update_course(course_id: int, data: CourseUpdate, service: CourseService = Depends(get_course_service)):
    """Actualizar un curso, no admite las lecciones en la misma petición"""
    return service.update_course(course_id, data)

@router.delete("/{course_id}", status_code=204)
def delete_course(course_id: int, service: CourseService = Depends(get_course_service)):
    """Eliminar un curso"""
    service.delete_course(course_id)
