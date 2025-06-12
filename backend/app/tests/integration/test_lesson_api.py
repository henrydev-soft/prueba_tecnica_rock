"""
Test de integración: gestión de lecciones

Este test valida la creación y consulta de lecciones asociadas a un curso existente.
Se utiliza el cliente de prueba de FastAPI (`TestClient`) para simular peticiones reales.

Se verifica:
- Que una lección válida se cree exitosamente.
- Que se pueda recuperar luego por su ID.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

import pytest

def test_create_and_get_lesson(client):
    # Paso 1: Crear un curso base
    course_response = client.post("/api/v1/courses/", json={
        "title": "Curso API",
        "description": "Curso de ejemplo",
        "instructor": "Henry"
    })
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Paso 2: Crear lección válida asociada
    lesson_response = client.post(f"/api/v1/courses/{course_id}/lessons/", json={
        "title": "Lección 1",
        "video_url": "https://youtube.com/watch?v=abc123"
    })
    assert lesson_response.status_code == 201
    lesson_data = lesson_response.json()

    assert lesson_data["title"] == "Lección 1"
    assert lesson_data["course_id"] == course_id
    lesson_id = lesson_data["id"]

    # Paso 3: Consultar la lección por ID
    get_response = client.get(f"/api/v1/lessons/{lesson_id}")
    assert get_response.status_code == 200
    get_data = get_response.json()

    assert get_data["id"] == lesson_id
    assert get_data["title"] == "Lección 1"
    assert get_data["course_id"] == course_id
