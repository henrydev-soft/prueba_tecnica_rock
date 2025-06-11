"""
Modelo ORM para la entidad Course

Define el modelo SQLAlchemy que representa la tabla 'courses'.
Establece la relación uno-a-muchos con las lecciones asociadas (LessonModel).

Autor: Henry Jimenez
Fecha: 2025-06-11
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base

class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    instructor = Column(String(100), nullable=False)

    lessons = relationship(
        "LessonModel",
        back_populates="course",
        cascade="all, delete",
        passive_deletes=True
    )
