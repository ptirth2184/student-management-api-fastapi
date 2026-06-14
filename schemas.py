from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
    email: str

class StudentResponse(StudentCreate):
    id: int
    name: str
    age: int
    course: str
    email: str

    model_config = ConfigDict(from_attributes=True)