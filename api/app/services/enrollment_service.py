from fastapi import HTTPException, status
from datetime import date
from typing import List

from app.repositories.enrollment import EnrollmentRepository
from app.repositories.student import StudentRepository
from app.repositories.career import CareerRepository
from app.repositories.study_plan import StudyPlanRepository
from app.repositories.classroom import ClassroomRepository
from app.schemas.enrollment import EnrollmentCreate, EnrollmentResponse, SubjectEnrollmentResponse, SubjectEnrollmentCreate
from app.models.enrollment import Enrollment
from app.models.enrollment_subject_classroom import EnrollmentSubjectClassroom
from app.core.exceptions import CourseFullError, CourseNotFoundError, AlreadyEnrolledError, StudentNotFoundError, CareerNotFoundError, StudyPlanNotFoundError, EnrollmentNotFoundError

class EnrollmentService:
    def __init__(
            self, 
            enrollment_repo: EnrollmentRepository,
            student_repo: StudentRepository,
            career_repo: CareerRepository,
            study_plan_repo: StudyPlanRepository,
            classroom_repo: ClassroomRepository
        ) -> None:
        self.repository = enrollment_repo
        self.student_repo = student_repo
        self.career_repo = career_repo
        self.study_plan_repo = study_plan_repo
        self.classroom_repo = classroom_repo

    def enroll_career(self, data: EnrollmentCreate) -> EnrollmentResponse:
        if not self.student_repo.get_by_id(data.student_id):
            raise StudentNotFoundError()
        
        career = self.career_repo.get_by_id(data.career_id)
        study_plan = self.study_plan_repo.get_by_id(data.study_plan_id)

        if not career:
            raise CareerNotFoundError()
        if not study_plan:
            raise StudyPlanNotFoundError()
        if study_plan.career_id != career.id:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Study plan and career do not match"
            )
        
        existing_enrollment = self.repository.get_by_student_career_study_plan(data.student_id, data.career_id, data.study_plan_id)
        if existing_enrollment:
            raise AlreadyEnrolledError()
        
        enrollment = Enrollment(
            student_id = data.student_id,
            career_id = data.career_id,
            study_plan_id = data.study_plan_id,
            enrollment_date = date.today()
        )

        return EnrollmentResponse.model_validate(self.repository.save(enrollment))
    
    def enroll_subject(self, data: SubjectEnrollmentCreate, enrollment_id: int) -> SubjectEnrollmentResponse:
        enrollment = self.repository.get_by_id( enrollment_id)
        if not enrollment:
            raise EnrollmentNotFoundError()
        
        classroom = self.classroom_repo.get_by_id(data.classroom_id)
        if not classroom:
            raise CourseNotFoundError()
        
        current_count = self.repository.get_subject_classroom_count(data.classroom_id)
        if current_count >= classroom.capacity:
            raise CourseFullError()
        
        duplicate = self.repository.get_subject_classroom_duplicate(enrollment_id, data.subject_study_plan_id)
        if duplicate:
            raise AlreadyEnrolledError()

        subjectClassroom = EnrollmentSubjectClassroom(
            enrollment_id = enrollment_id,
            subject_study_plan_id = data.subject_study_plan_id,
            classroom_id = data.classroom_id
        )

        return SubjectEnrollmentResponse.model_validate(self.repository.save_subject_classroom(subjectClassroom))
    
    def list_by_student(self, student_id: int) -> List[EnrollmentResponse]:
        if not self.student_repo.get_by_id(student_id):
            raise StudentNotFoundError()
        
        enrollments = self.repository.get_by_student(student_id)
        return [EnrollmentResponse.model_validate(enrollment) for enrollment in enrollments]
        
