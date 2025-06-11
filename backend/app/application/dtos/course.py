"""
Course DTOs

Este módulo define los modelos Pydantic utilizados como Data Transfer Objects (DTOs)
para la entidad Course. Estos modelos son empleados para la validación y estructuración
de datos en las operaciones de entrada y salida a través de la API.

Modelos definidos:
- CourseBase: Modelo base con los campos comunes.
- CourseCreate: Modelo para la creación de cursos (POST).
- CourseUpdate: Modelo para la actualización parcial o total de un curso (PUT).
- CourseRead: Modelo para la lectura de un curso individual.
- CourseWithLessons: Modelo extendido que incluye las lecciones del curso.

Estos DTOs son independientes de los modelos de dominio y de infraestructura, y 
siguen el principio de separación de responsabilidades, facilitando la validación
y documentación automática en FastAPI.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from typing import List, Optional
from pydantic import BaseModel, field_validator

from .lesson import LessonRead

# Funciones Auxiliares de Validación
# Si el modelo de datos de la aplicación se hace más grande se puede mover a un módulo compartido de validación
# en app/core/validators.py para tener un lugar central de validaciones reutilizables. 

def check_max_length(field: str, value: str, max_len: int) -> str:
    if len(value) > max_len:
        raise ValueError(f"El campo '{field}' no debe exceder {max_len} caracteres.")
    return value

class CourseBase(BaseModel):
    title: str
    description: str
    instructor: str
    
    @field_validator("title")
    @classmethod
    def validate_title_length(cls, v: str) -> str:
        return check_max_length("title", v, 100)

    @field_validator("description")
    @classmethod
    def validate_description_length(cls, v: str) -> str:
        return check_max_length("description", v, 500)

    @field_validator("instructor")
    @classmethod
    def validate_instructor_length(cls, v: str) -> str:
        return check_max_length("instructor", v, 100)



class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    instructor: Optional[str] = None

    @field_validator("title")
    @classmethod
    def validate_title_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return check_max_length("title", v, 100)
        return v

    @field_validator("description")
    @classmethod
    def validate_description_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return check_max_length("description", v, 500)
        return v

    @field_validator("instructor")
    @classmethod
    def validate_instructor_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return check_max_length("instructor", v, 100)
        return v

class CourseRead(CourseBase):
    id: int
    
    model_config = {
        "from_attributes": True
    }

class CourseWithLessons(CourseRead):
    lessons: List[LessonRead] = []