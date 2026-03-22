from fastapi import HTTPException, status

from app.repositories.classroom import ClassroomRepository
from app.schemas.classroom import ClassroomCreate, ClassroomResponse
from app.models.classroom import Classroom

class CourseService:
    def __init__(self, repo: ClassroomRepository):
        self.repo = repo

    def create(self, data: ClassroomCreate) -> ClassroomResponse:
        classroom = Classroom(
            classroom_number = self.repo.get_next_number(),
            capacity = data.capacity
        )

        return ClassroomResponse.model_validate(self.repo.save(classroom))
        