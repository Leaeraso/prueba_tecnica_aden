from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.classroom import ClassroomRepository
from app.services.classroom_service import CourseService
from app.schemas.classroom import ClassroomCreate, ClassroomResponse

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_course_service(db: Session = Depends(get_db)) -> CourseService:
      return CourseService(repo=ClassroomRepository(db))


@router.post("", response_model=ClassroomResponse, status_code=status.HTTP_201_CREATED)
def create_course(data: ClassroomCreate, service: CourseService = Depends(get_course_service)):
    return service.create(data)