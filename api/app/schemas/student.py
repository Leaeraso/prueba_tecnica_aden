from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    dni: Optional[int] = None
    date_of_birth: Optional[date] = None


class StudentStatusResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class StudentResponse(BaseModel):
    id: int
    student_number: int
    name: str
    last_name: str
    email: str
    status: StudentStatusResponse

    model_config = {"from_attributes": True}
