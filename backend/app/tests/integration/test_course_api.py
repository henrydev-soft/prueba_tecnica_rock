"""
Test de integración: crear curso y obtenerlo

Verifica que la API REST permita crear un curso y luego recuperarlo exitosamente
mediante los endpoints definidos en `routes.course`.

Confirma la integración entre routers, servicios, repositorios y base de datos.


Autor: Henry Jiménez
Fecha: 2025-06-11
"""

import pytest

def test_create_and_get_course(client):
    create_resp = client.post("/api/v1/courses/", json={
        "title": "Curso Test",
        "description": "Desc",
        "instructor": "Henry"
    })

    assert create_resp.status_code == 201
    course_id = create_resp.json()["id"]

    get_resp = client.get(f"/api/v1/courses/{course_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["title"] == "Curso Test"
    assert data["lessons"] == []
