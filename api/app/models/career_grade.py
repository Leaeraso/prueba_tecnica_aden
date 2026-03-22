from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class CareerGrade(Base):
    __tablename__ = "career_grades"

    career_id = Column(Integer, ForeignKey("careers.id"), primary_key=True, index=True)
    grade_id = Column(Integer, ForeignKey("grades.id"), primary_key=True, index=True)

    career = relationship("Career", back_populates="grades")
    grade = relationship("Grade", back_populates="grades")