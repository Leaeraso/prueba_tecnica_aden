from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    study_plans = relationship("SubjectStudyPlan", back_populates="subject")
    professors = relationship("ProfessorSubject", back_populates="subject")
