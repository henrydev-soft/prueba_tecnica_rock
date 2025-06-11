"""
Excepciones personalizadas para la aplicación

Define clases de error específicas del dominio y utilidades para devolver
respuestas HTTP estructuradas desde los endpoints.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from fastapi import HTTPException, status


class AppException(Exception):
    """Clase base para excepciones controladas de la aplicación."""
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)


class CourseNotFound(AppException):
    """Se lanza cuando un curso no existe."""
    def __init__(self, course_id: int):
        super().__init__(f"Curso con ID {course_id} no encontrado.")
        self.course_id = course_id


class LessonNotFound(AppException):
    """Se lanza cuando una lección no existe."""
    def __init__(self, lesson_id: int):
        super().__init__(f"Lección con ID {lesson_id} no encontrada.")
        self.lesson_id = lesson_id

def http_400(detail: str = "Solicitud inválida"):
    """Shortcut para lanzar 400 HTTPException."""
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

def http_401(detail: str = "No autorizado"):
    """Shortcut para lanzar 401 HTTPException."""
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

def http_403(detail: str = "Acceso prohibido"):
    """Shortcut para lanzar 403 HTTPException."""
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

def http_404(detail: str = "No encontrado"):
    """Shortcut para lanzar 404 HTTPException."""
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

def http_409(detail: str = "Conflicto de datos"):
    """Shortcut para lanzar 409 HTTPException."""
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)

def http_422(detail: str = "Entidad no procesable"):
    """Shortcut para lanzar 422 HTTPException."""
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)

def http_500(detail: str = "Error interno del servidor"):
    """Shortcut para lanzar 500 HTTPException."""
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
