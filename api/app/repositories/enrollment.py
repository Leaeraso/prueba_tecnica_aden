from sqlalchemy.orm import Session
from typing import Optional, List

from app.models.enrollment import Enrollment
from app.models.enrollment_subject_classroom import EnrollmentSubjectClassroom
from app.repositories.base import BaseRepository

class EnrollmentRepository(BaseRepository[Enrollment]):
    def __init__(self, db: Session):
        super().__init__(Enrollment, db)

    def get_by_student_career_study_plan(self, student_id: int, career_id: int, study_plan_id: int) -> Optional[Enrollment]:
        return self.db.query(Enrollment).filter(
            Enrollment.student_id == student_id,
            Enrollment.career_id == career_id, 
            Enrollment.study_plan_id == study_plan_id
        ).first()
    
    def get_subject_classroom_count(self, classroom_id: int) -> int:
        return self.db.query(EnrollmentSubjectClassroom).filter(
            EnrollmentSubjectClassroom.classroom_id == classroom_id
        ).count()
    
    def get_subject_classroom_duplicate(self, enrollment_id: int, subject_study_plan_id: int) -> Optional[EnrollmentSubjectClassroom]:
        return self.db.query(EnrollmentSubjectClassroom).filter(
            EnrollmentSubjectClassroom.enrollment_id == enrollment_id,
            EnrollmentSubjectClassroom.subject_study_plan_id == subject_study_plan_id
        ).first()
    
    def save_subject_classroom(self, instace: EnrollmentSubjectClassroom) -> EnrollmentSubjectClassroom:
        self.db.add(instace)
        self.db.commit()
        self.db.refresh(instace)
        return instace
    
    def get_by_student(self, student_id: int) -> List[Enrollment]:
        return self.db.query(Enrollment).filter(
            Enrollment.student_id == student_id
        ).all()

