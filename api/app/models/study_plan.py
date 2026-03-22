from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    career_id = Column(Integer, ForeignKey("careers.id"), nullable=False)

    career = relationship("Career", back_populates="study_plans")
    subjects = relationship("SubjectStudyPlan", back_populates="study_plan")
    enrollments = relationship("Enrollment", back_populates="study_plan")
