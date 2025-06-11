"""
Lesson DTOs

Este módulo contiene los modelos Pydantic que actúan como Data Transfer Objects (DTOs)
para la entidad Lesson. Su propósito es definir claramente las estructuras utilizadas
para recibir y devolver datos relacionados con lecciones en la API REST.

Modelos definidos:
- LessonBase: Modelo base con los campos comunes.
- LessonCreate: Modelo para crear nuevas lecciones (POST).
- LessonUpdate: Modelo para modificar datos de una lección existente (PUT).
- LessonRead: Modelo para representar una lección al ser leída desde la API (GET).

Los DTOs permiten desacoplar las estructuras de datos de la lógica de negocio
y del ORM, promoviendo un diseño limpio y mantenible.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from typing import Optional
from pydantic import BaseModel, HttpUrl, field_validator


# Funciones Auxiliares de Validación
# Si el modelo de datos de la aplicación se hace más grande se puede mover a un módulo compartido de validación
# en app/core/validators.py para tener un lugar central de validaciones reutilizables. 

def is_valid_youtube_url(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url

def check_max_length(field: str, value: str, max_len: int) -> str:
    if len(value) > max_len:
        raise ValueError(f"El campo '{field}' no debe exceder {max_len} caracteres.")
    return value


class LessonBase(BaseModel):
    title: str
    video_url: HttpUrl

    @field_validator("title")
    @classmethod
    def validate_title_length(cls, v: str) -> str:
        return check_max_length("title", v, 100)

    @field_validator("video_url")
    @classmethod
    def validate_youtube_url(cls, v: HttpUrl) -> HttpUrl:
        if not is_valid_youtube_url(str(v)):
            raise ValueError("La URL debe ser un enlace válido de YouTube.")
        return check_max_length("video_url", str(v), 500)

class LessonCreate(LessonBase):
    pass

class LessonUpdate(BaseModel):
    title: Optional[str] = None
    video_url: Optional[HttpUrl] = None

    @field_validator("title")
    @classmethod
    def validate_title_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return check_max_length("title", v, 100)
        return v

    @field_validator("video_url")
    @classmethod
    def validate_youtube_url(cls, v: Optional[HttpUrl]) -> Optional[HttpUrl]:
        if v is not None:
            url_str = str(v)
            if not is_valid_youtube_url(url_str):
                raise ValueError("La URL debe ser un enlace válido de YouTube.")
            return check_max_length("video_url", url_str, 500)
        return v

class LessonRead(LessonBase):
    id: int
    course_id: int

    class Config: 
        orm_mode = True