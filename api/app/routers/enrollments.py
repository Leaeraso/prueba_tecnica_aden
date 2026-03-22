from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.repositories.enrollment import EnrollmentRepository
from app.repositories.student import StudentRepository
from app.repositories.career import CareerRepository
from app.repositories.study_plan import StudyPlanRepository
from app.repositories.classroom import ClassroomRepository
from app.services.enrollment_service import EnrollmentService
from app.schemas.enrollment import (
    EnrollmentCreate, EnrollmentResponse,
    SubjectEnrollmentCreate, SubjectEnrollmentResponse,
)

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


def get_enrollment_service(db: Session = Depends(get_db)) -> EnrollmentService:
    return EnrollmentService(
        enrollment_repo=EnrollmentRepository(db),
        student_repo=StudentRepository(db),
        career_repo=CareerRepository(db),
        study_plan_repo=StudyPlanRepository(db),
        classroom_repo=ClassroomRepository(db),
    )


@router.post("", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_career(data: EnrollmentCreate, service: EnrollmentService = Depends(get_enrollment_service)):
    return service.enroll_career(data)


@router.post("/{enrollment_id}/subjects", response_model=SubjectEnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_subject(enrollment_id: int, data: SubjectEnrollmentCreate, service: EnrollmentService =
Depends(get_enrollment_service)):
    return service.enroll_subject(data, enrollment_id)


@router.get("/student/{student_id}", response_model=List[EnrollmentResponse])
def list_student_enrollments(student_id: int, service: EnrollmentService = Depends(get_enrollment_service)):
    return service.list_by_student(student_id)