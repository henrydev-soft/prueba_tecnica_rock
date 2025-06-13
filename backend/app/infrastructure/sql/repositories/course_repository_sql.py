"""
Implementación del repositorio de cursos con SQLAlchemy

Este módulo implementa la interfaz ICourseRepository utilizando SQLAlchemy
para realizar operaciones de persistencia sobre la entidad Course.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""

from sqlalchemy.orm import Session
from app.domain.models.course import Course, Lesson
from app.domain.repositories import ICourseRepository
from app.infrastructure.sql import CourseModel, LessonModel

class SQLCourseRepository(ICourseRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Course]:
        courses = self.db.query(CourseModel).all()
        return [self._to_domain(c) for c in courses]

    def get_by_id(self, course_id: int) -> Course | None:
        course_model = self.db.query(CourseModel).filter(CourseModel.id == course_id).first()
        return self._to_domain(course_model) if course_model else None

    def create(self, course: Course) -> Course:
        course_model = self._to_model(course)
        self.db.add(course_model)
        self.db.commit()
        self.db.refresh(course_model)
        return self._to_domain(course_model)

    def update(self, course: Course) -> Course:
        existing = self.db.query(CourseModel).filter(CourseModel.id == course.id).first()
        if not existing:
            return None
        existing.title = course.title
        existing.description = course.description
        existing.instructor = course.instructor
        self.db.commit()
        self.db.refresh(existing)
        return self._to_domain(existing)

    def delete(self, course: Course) -> None:
        course_model = self.db.query(CourseModel).filter(CourseModel.id == course.id).first()
        if course_model:
            self.db.delete(course_model)
            self.db.commit()
    
    def _to_domain(self, course_model: CourseModel) -> Course:
        return Course(
            id=course_model.id,
            title=course_model.title,
            description=course_model.description,
            instructor=course_model.instructor,
            lessons=[
                Lesson(id=l.id, title=l.title, video_url=l.video_url, course_id=l.course.id)
                for l in course_model.lessons
            ]
        )

    def _to_model(self, course: Course) -> CourseModel:
        return CourseModel(
            id=course.id,
            title=course.title,
            description=course.description,
            instructor=course.instructor,
            lessons=[
                LessonModel(
                    id=lesson.id,
                    title=lesson.title,
                    video_url=lesson.video_url,
                    course_id=course.id
                ) for lesson in course.lessons
            ]
        )
