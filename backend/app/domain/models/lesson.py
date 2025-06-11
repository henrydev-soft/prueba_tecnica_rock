"""
Lesson Entity

Este módulo define la entidad de dominio `Lesson`, la cual representa una lección que
pertenece a un curso. Cada lección contiene un título, una URL de video (por ejemplo,
de YouTube) y una referencia al curso al que pertenece.

Esta entidad se mantiene libre de dependencias tecnológicas externas y está diseñada
para ser utilizada dentro de la lógica del dominio de la aplicación.

Responsabilidades:
- Representar una unidad de contenido dentro de un curso.
- Actuar como modelo base en los servicios de aplicación y repositorios.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

class Lesson: 
    def __init__(self, id: int, title: str, video_url: str, course_id: int):
        self.id = id
        self.title = title
        self.video_url = video_url
        self.course_id = course_id
