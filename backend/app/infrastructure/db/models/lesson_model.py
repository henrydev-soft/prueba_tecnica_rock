"""
Modelo ORM para la entidad Lesson

Define el modelo SQLAlchemy que representa la tabla 'lessons'.
Establece la relación muchos-a-uno con un curso (CourseModel).

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base

class LessonModel(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    video_url = Column(String(500), nullable=False)

    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)

    course = relationship("CourseModel", back_populates="lessons")
