from sqlalchemy.orm import Session
from app.domain.models.course import Course
from app.domain.repositories.course_repo import ICourseRepository
from app.infrastructure.db.models.course_model import CourseModel
from app.infrastructure.db.models.lesson_model import LessonModel

class CourseRepository(ICourseRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[CourseModel]:
        return self.db.query(CourseModel).all()

    def get_by_id(self, course_id: int) -> CourseModel | None:
        return self.db.query(CourseModel).filter(CourseModel.id == course_id).first()

    def create(self, course: CourseModel) -> CourseModel:
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def update(self, course: CourseModel) -> CourseModel:
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete(self, course: CourseModel) -> None:
        self.db.delete(course)
        self.db.commit()
