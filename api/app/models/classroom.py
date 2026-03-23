from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    classroom_number = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)

    enrollments = relationship("EnrollmentSubjectClassroom", back_populates="classroom")
