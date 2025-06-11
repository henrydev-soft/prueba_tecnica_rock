"""
Test unitario: crear curso usando repositorio simulado

Verifica que el servicio `CourseService` pueda crear un curso correctamente
cuando se le proporciona un DTO válido, y que interactúe con el repositorio mockeado.

Este test no depende de base de datos ni de FastAPI.


Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from app.application.services import CourseService
from app.infrastructure.db.models import CourseModel
from app.application.dtos.course import CourseCreate
from unittest.mock import MagicMock
import pytest

def test_create_course():
    mock_repo = MagicMock()
    service = CourseService(mock_repo)
    
    data = CourseCreate(
        title="Curso de FastAPI",
        description="Aprende APIs modernas",
        instructor="Henry"
    )

    # Simula el retorno del ORM
    mock_repo.create.return_value = CourseModel(id=1, **data.model_dump())

    result = service.create_course(data)

    assert result.id == 1
    assert result.title == "Curso de FastAPI"
    mock_repo.create.assert_called_once()
