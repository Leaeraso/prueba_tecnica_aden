from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ProfessorSubject(Base):
    __tablename__ = "professor_subjects"

    professor_id = Column(Integer, ForeignKey("professors.id"), primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), primary_key=True)

    professor = relationship("Professor", back_populates="subjects")
    subject = relationship("Subject", back_populates="professors")
