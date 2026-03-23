from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.student import StudentRepository
from app.repositories.student_status import StudentStatusRepository
from app.services.student_service import StudentService
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


def get_student_service(db: Session = Depends(get_db)) -> StudentService:
    return StudentService(
        repo=StudentRepository(db),
        status_repo=StudentStatusRepository(db),
    )


@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(data: StudentCreate, service: StudentService = Depends(get_student_service)):
    return service.create(data)