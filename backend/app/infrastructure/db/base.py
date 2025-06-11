"""
Base ORM

Este módulo define la clase base declarativa de SQLAlchemy que será utilizada como
superclase para todos los modelos ORM del proyecto.

Al heredar de `Base`, cada modelo se registra automáticamente en el sistema
de metadatos de SQLAlchemy, permitiendo su descubrimiento por herramientas
como Alembic para la gestión de migraciones.

Este archivo forma parte de la infraestructura del sistema, y permite desacoplar
la lógica de persistencia del dominio de negocio, siguiendo los principios
de la arquitectura hexagonal.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Clase base abstracta para todos los modelos ORM.
    """
    pass