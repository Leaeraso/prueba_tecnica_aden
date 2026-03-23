from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class SubjectStudyPlan(Base):
    __tablename__ = "subject_study_plans"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    study_plan_id = Column(Integer, ForeignKey("study_plans.id"), nullable=False)
    grade_id = Column(Integer, ForeignKey("grades.id"), nullable=False)

    subject = relationship("Subject", back_populates="study_plans")
    study_plan = relationship("StudyPlan", back_populates="subjects")
    grade = relationship("Grade", back_populates="study_plans")
    enrollment_subject_classrooms = relationship("EnrollmentSubjectClassroom", back_populates="subject_study_plan")
