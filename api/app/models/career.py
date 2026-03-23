from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Career(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    grades = relationship("CareerGrade", back_populates="career")
    study_plans = relationship("StudyPlan", back_populates="career")
    enrollments = relationship("Enrollment", back_populates="career")
