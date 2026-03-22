from sqlalchemy.orm import Session
from typing import Optional

from app.models.student import Student
from app.repositories.base import BaseRepository
from app.core.config import settings

class StudentRepository(BaseRepository[Student]):
    def __init__(self, db: Session):
        super().__init__(Student, db)

    def get_by_email(self, email: str) -> Optional[Student]:
        return self.db.query(Student).filter(Student.email == email).first()

    def get_next_number(self) -> int:
        last = self.db.query(Student).order_by(Student.student_number.desc()).first()
        return last.student_number + 1 if last else settings.student_number_start
    
