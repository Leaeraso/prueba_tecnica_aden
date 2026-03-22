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
    # student_number y status_id los asigna el servicio automáticamente

class StudentResponse(BaseModel):
    id: int
    student_number: int
    name: str
    last_name: str
    email: str
    status_id: int

    model_config = {"from_attributes": True}