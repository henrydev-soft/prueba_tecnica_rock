"""
Test unitario: validación de URL de lección

Verifica que el DTO `LessonCreate` rechace correctamente una URL que no
pertenezca a YouTube. La validación se hace mediante Pydantic y lanza
una excepción de tipo `ValidationError`.

Esto permite prevenir datos incorrectos desde el ingreso.


Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from unittest.mock import MagicMock
from app.application.services import LessonService
from app.application.dtos.lesson import LessonCreate
from app.core.exceptions import CourseNotFound, LessonNotFound
from app.domain.models import Lesson
from app.domain.models import Course
from pydantic import ValidationError
import pytest

def test_create_lesson_for_course():
    """ Test para verificar la creación de una lección en un curso existente"""
    mock_lesson_repo = MagicMock()
    mock_course_repo = MagicMock()
    service = LessonService(mock_lesson_repo, mock_course_repo)

    mock_course_repo.get_by_id.return_value = Course(id=1, title="Curso", description="Desc", instructor="Henry")
    lesson_data = LessonCreate(title="Intro", video_url="https://youtube.com/watch?v=abc123")

    mock_lesson_repo.create.return_value = Lesson(id=1, course_id=1, **lesson_data.model_dump())

    result = service.create_lesson(1, lesson_data)

    assert result.id == 1
    assert result.title == "Intro"
    mock_lesson_repo.create.assert_called_once()
    mock_course_repo.get_by_id.assert_called_once_with(1)

def test_create_lesson_course_not_found():
    """ Test para verificar la creación de una lección en un curso no existente"""
    mock_lesson_repo = MagicMock()
    mock_course_repo = MagicMock()
    service = LessonService(mock_lesson_repo, mock_course_repo)

    mock_course_repo.get_by_id.return_value = None

    lesson_data = LessonCreate(title="Intro", video_url="https://youtube.com/watch?v=xyz")

    with pytest.raises(CourseNotFound):
        service.create_lesson(999, lesson_data)

    mock_course_repo.get_by_id.assert_called_once_with(999)

def test_get_lesson_by_id_success():
    """ Test para obtener una lección por su id"""
    mock_lesson_repo = MagicMock()
    mock_course_repo = MagicMock()
    service = LessonService(mock_lesson_repo, mock_course_repo)

    lesson = Lesson(id=1, course_id=1, title="Intro", video_url="https://youtube.com/watch?v=abc")
    mock_lesson_repo.get_by_id.return_value = lesson

    result = service.get_lesson(1)

    assert result.id == 1
    assert result.title == "Intro"
    mock_lesson_repo.get_by_id.assert_called_once_with(1)


def test_get_lesson_by_id_not_found():
    """ Test para obtener una lección no existente por su id"""
    mock_lesson_repo = MagicMock()
    mock_course_repo = MagicMock()
    service = LessonService(mock_lesson_repo, mock_course_repo)

    mock_lesson_repo.get_by_id.return_value = None

    with pytest.raises(LessonNotFound):
        service.get_lesson(999)

    mock_lesson_repo.get_by_id.assert_called_once_with(999)


def test_reject_invalid_youtube_url():
    """ Test para validar creación de lección con url inválida para youtube"""
    with pytest.raises(ValidationError) as exc_info:
        LessonCreate(
            title="Lección",
            video_url="https://google.com"
        )
    assert "YouTube" in str(exc_info.value)
