"""
Excepciones personalizadas para la aplicación

Define clases de error específicas para ser lanzadas a lo largo de la aplicación

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

class AppException(Exception):
    """Clase base para excepciones controladas de la aplicación."""
    def __init__(self, detail: str, status_code: int = 400):
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)


class CourseNotFound(AppException):
    """Se lanza cuando un curso no existe."""
    def __init__(self, course_id: int):
        super().__init__(f"Curso con ID {course_id} no encontrado.", status_code = 404)
        self.course_id = course_id

class LessonNotFound(AppException):
    """Se lanza cuando una lección no existe."""
    def __init__(self, lesson_id: int):
        super().__init__(f"Lección con ID {lesson_id} no encontrada.", status_code = 404)
        self.lesson_id = lesson_id

class ForbiddenAccess(AppException):
    """Acceso prohibido (403)."""
    def __init__(self, detail: str = "No tienes permiso para acceder a este recurso."):
        super().__init__(detail, status_code=403)

class NotAcceptable(AppException):
    """No aceptable (406)."""
    def __init__(self, detail: str = "El recurso solicitado no puede ser entregado en el formato solicitado."):
        super().__init__(detail, status_code=406)

class RequestTimeout(AppException):
    """Tiempo de espera agotado (408)."""
    def __init__(self, detail: str = "El servidor agotó el tiempo de espera de la solicitud."):
        super().__init__(detail, status_code=408)

class Conflict(AppException):
    """Conflicto de datos (409)."""
    def __init__(self, detail: str = "Conflicto con el estado actual del recurso."):
        super().__init__(detail, status_code=409)