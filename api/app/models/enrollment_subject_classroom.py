from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class EnrollmentSubjectClassroom(Base):
    __tablename__ = "enrollment_subject_classrooms"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.id"), nullable=False)
    subject_study_plan_id = Column(Integer, ForeignKey("subject_study_plans.id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)

    enrollment = relationship("Enrollment", back_populates="subject_classrooms")
    subject_study_plan = relationship("SubjectStudyPlan", back_populates="enrollment_subject_classrooms")
    classroom = relationship("Classroom", back_populates="enrollments")
