"""
Test unitario: validación de URL de lección

Verifica que el DTO `LessonCreate` rechace correctamente una URL que no
pertenezca a YouTube. La validación se hace mediante Pydantic y lanza
una excepción de tipo `ValidationError`.

Esto permite prevenir datos incorrectos desde el ingreso.


Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from app.application.dtos.lesson import LessonCreate
import pytest
from pydantic import ValidationError

def test_reject_invalid_youtube_url():
    with pytest.raises(ValidationError) as exc_info:
        LessonCreate(
            title="Lección",
            video_url="https://google.com"
        )
    assert "YouTube" in str(exc_info.value)
