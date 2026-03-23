from pydantic import BaseModel
from datetime import date


class NamedEntityResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class CareerResponse(NamedEntityResponse):
    pass


class StudyPlanResponse(NamedEntityResponse):
    pass


class SubjectNestedResponse(NamedEntityResponse):
    pass


class GradeNestedResponse(NamedEntityResponse):
    pass


class ClassroomNestedResponse(BaseModel):
    id: int
    classroom_number: int
    capacity: int

    model_config = {"from_attributes": True}


class SubjectStudyPlanNestedResponse(BaseModel):
    id: int
    subject: SubjectNestedResponse
    grade: GradeNestedResponse

    model_config = {"from_attributes": True}


class EnrollmentSubjectClassroomResponse(BaseModel):
    id: int
    subject_study_plan: SubjectStudyPlanNestedResponse
    classroom: ClassroomNestedResponse

    model_config = {"from_attributes": True}


class EnrollmentCreate(BaseModel):
    student_id: int
    career_id: int
    study_plan_id: int


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    career: CareerResponse
    study_plan: StudyPlanResponse
    enrollment_date: date
    subject_classrooms: list[EnrollmentSubjectClassroomResponse]

    model_config = {"from_attributes": True}


class SubjectEnrollmentCreate(BaseModel):
    subject_study_plan_id: int
    classroom_id: int


class SubjectEnrollmentResponse(BaseModel):
    id: int
    enrollment_id: int
    subject_study_plan: SubjectStudyPlanNestedResponse
    classroom: ClassroomNestedResponse

    model_config = {"from_attributes": True}
