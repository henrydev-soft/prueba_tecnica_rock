"""
Test unitario: crear curso usando repositorio simulado

Verifica que el servicio `CourseService` pueda crear un curso correctamente
cuando se le proporciona un DTO válido, y que interactúe con el repositorio mockeado.

Este test no depende de base de datos ni de FastAPI.


Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from app.application.services import CourseService
from app.domain.models import Course
from app.application.dtos.course import CourseCreate, CourseUpdate
from app.core.exceptions import CourseNotFound
from unittest.mock import MagicMock
import pytest


def test_create_course():
    """ Test para verificar la creación de un curso"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)
    
    data = CourseCreate(
        title="Curso de FastAPI",
        description="Aprende APIs modernas",
        instructor="Henry"
    )

    mock_repo.create.return_value = Course(id=1, **data.model_dump())

    result = service.create_course(data)

    assert result.id == 1
    assert result.title == "Curso de FastAPI"
    mock_repo.create.assert_called_once()

def test_get_course_by_id_found():
    """ Test para obtener un curso por su id"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)
    
    fake_course = Course(id=1, title="Curso", description="Desc", instructor="Henry")
    mock_repo.get_by_id.return_value = fake_course

    result = service.get_course(1)

    assert result.id == 1
    assert result.title == "Curso"
    mock_repo.get_by_id.assert_called_once_with(1)


def test_get_course_by_id_not_found():
    """ Test para obtener un curso no existente por su id"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)

    mock_repo.get_by_id.return_value = None

    with pytest.raises(CourseNotFound) as exc:
        service.get_course(999)

    assert "Curso con ID 999 no encontrado." in str(exc.value)


def test_update_course():
    """ Test para actualizar un curso"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)

    original = Course(id=1, title="Viejo", description="Desc", instructor="Henry")
    updated_data = CourseUpdate(title="Nuevo", description="Nuevo Desc", instructor="Henry")

    mock_repo.get_by_id.return_value = original
    mock_repo.update.return_value = Course(id=1, **updated_data.model_dump())

    result = service.update_course(1, updated_data)

    assert result.title == "Nuevo"
    mock_repo.update.assert_called_once()

def test_update_course_not_found():
    """ Test para actualizar un curso no existente"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)

    mock_repo.get_by_id.return_value = None

    with pytest.raises(CourseNotFound):
        service.update_course(42, CourseUpdate(title="X", description="Y", instructor="Z"))


def test_delete_course():
    """ Test para eliminar un curso"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)

    mock_repo.get_by_id.return_value = Course(id=1, title="Curso", description="Desc", instructor="Henry")

    service.delete_course(1)

    mock_repo.delete.assert_called_once_with(
        Course(id=1, title="Curso", description="Desc", instructor="Henry")
    )



def test_list_courses():
    """ Test para listar cursos"""
    mock_repo = MagicMock()
    service = CourseService(mock_repo)

    mock_repo.get_all.return_value = [
        Course(id=1, title="A", description="...", instructor="X"),
        Course(id=2, title="B", description="...", instructor="Y")
    ]

    results = service.list_courses()

    assert len(results) == 2
    mock_repo.get_all.assert_called_once()
