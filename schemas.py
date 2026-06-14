from pydantic import BaseModel, Field, ConfigDict

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., ge=18)
    course: str = Field(..., min_length=2)
    email: str = Field(...)

class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)