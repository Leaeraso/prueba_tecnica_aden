from pydantic import BaseModel
from datetime import date

class EnrollmentCreate(BaseModel):
    student_id: int
    career_id: int
    study_plan_id: int


class EnrollmentSubjectClassroomResponse(BaseModel):
    id: int
    enrollment_id: int
    subject_study_plan_id: int
    classroom_id: int

    model_config = {"from_attributes": True}


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    career_id: int
    study_plan_id: int
    enrollment_date: date
    subjects: list[EnrollmentSubjectClassroomResponse]

    model_config = {"from_attributes": True}


class SubjectEnrollmentCreate(BaseModel):
    subject_study_plan_id: int
    classroom_id: int


class SubjectEnrollmentResponse(BaseModel):
    id: int
    enrollment_id: int
    subject_study_plan_id: int
    classroom_id: int

    model_config = {"from_attributes": True}
