from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.core.database import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_date = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    career_id = Column(Integer, ForeignKey("careers.id"), nullable=False)
    study_plan_id = Column(Integer, ForeignKey("study_plans.id"), nullable=False)

    student = relationship("Student", back_populates="enrollments")
    career = relationship("Career", back_populates="enrollments")
    study_plan = relationship("StudyPlan", back_populates="enrollments")
    subject_classrooms = relationship("EnrollmentSubjectClassroom", back_populates="enrollment")
