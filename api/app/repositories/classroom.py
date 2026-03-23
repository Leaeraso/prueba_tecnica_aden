from sqlalchemy.orm import Session
from typing import Optional

from app.models.classroom import Classroom
from app.repositories.base import BaseRepository
from app.core.config import settings

class ClassroomRepository(BaseRepository[Classroom]):
    def __init__(self, db: Session):
        super().__init__(Classroom, db)

    def get_next_number(self) -> int:
        last = self.db.query(Classroom).order_by(Classroom.classroom_number.desc()).first()
        return last.classroom_number + 1 if last else settings.classroom_number_start