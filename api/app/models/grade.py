from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    grades = relationship("CareerGrade", back_populates="grade")
    study_plans = relationship("SubjectStudyPlan", back_populates="grade")
