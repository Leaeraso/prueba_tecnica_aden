from sqlalchemy.orm import Session
from typing import Optional

from app.models.student_status import StudentStatus
from app.repositories.base import BaseRepository

class StudentStatusRepository(BaseRepository[StudentStatus]):
    def __init__(self, db: Session):
        super().__init__(StudentStatus, db)

    def get_by_name(self, name: str) -> Optional[StudentStatus]:
        return self.db.query(StudentStatus).filter(StudentStatus.name == name).first()