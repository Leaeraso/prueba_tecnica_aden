from pydantic import BaseModel, Field

class ClassroomCreate(BaseModel):
    capacity: int = Field(gt=0)

class ClassroomResponse(BaseModel):
    id: int
    classroom_number: int
    capacity: int

    model_config = {"from_attributes": True}