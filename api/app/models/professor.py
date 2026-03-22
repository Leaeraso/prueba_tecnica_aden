from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.core.database import Base


class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True, index=True)
    professor_number = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    cuit = Column(Integer, nullable=True, unique=True)
    date_of_birth = Column(Date, nullable=True)

    subjects = relationship("ProfessorSubject", back_populates="professor")
