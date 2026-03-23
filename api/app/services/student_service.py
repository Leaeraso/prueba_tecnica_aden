from fastapi import HTTPException, status

from app.repositories.student import StudentRepository
from app.repositories.student_status import StudentStatusRepository
from app.core.security import hash_password
from app.schemas.student import StudentCreate, StudentResponse
from app.models.student import Student
from app.core.exceptions import StudentAlreadyExists

class StudentService:
    def __init__(self, repo: StudentRepository, status_repo: StudentStatusRepository):
        self.repo = repo
        self.status_repo = status_repo

    def create(self, data: StudentCreate) -> StudentResponse:
        if self.repo.get_by_email(data.email):
            raise StudentAlreadyExists()
        
        active_status = self.status_repo.get_by_name("active")
        if not active_status:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Active student status not found"
            )
        
        student = Student(
            student_number=self.repo.get_next_number(),
            name=data.name,
            last_name=data.last_name,
            email=data.email,
            hashed_password=hash_password(data.password),
            dni=data.dni,
            date_of_birth=data.date_of_birth,
            status_id=active_status.id
        )

        return StudentResponse.model_validate(self.repo.save(student))