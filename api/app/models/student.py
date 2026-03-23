from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_number = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    dni = Column(Integer, nullable=True, unique=True)
    date_of_birth = Column(Date, nullable=True)
    status_id = Column(Integer, ForeignKey("student_statuses.id"), nullable=False)

    status = relationship("StudentStatus", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")
