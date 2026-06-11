from typing import Dict, List

from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel, Field


app = FastAPI(title="Student Management API")


students = {}  # type: Dict[int, StudentResponse]
next_id = 1

# Request model for creating a student
class StudentCreate(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    course: str = Field(min_length=2)
    email: str = Field(...)

# Response model for student with ID
class StudentResponse(StudentCreate):
    id: int 
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    course: str = Field(min_length=2)
    email: str = Field(...)

# Create a student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> StudentResponse:
    global next_id
    new_student = StudentResponse(id=next_id, **student.model_dump())
    students[next_id] = new_student
    next_id += 1
    return new_student

# Search students by course
@app.get("/students/search", response_model=List[StudentResponse])
def search_students(course: str) -> List[StudentResponse]:
    return [student for student in students.values() if course.lower() in student.course.lower()]


# Get all students
@app.get("/students", response_model=List[StudentResponse])
def get_students() -> List[StudentResponse]:
    return list(students.values())

# Get a student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int = Path(..., gt=0)) -> StudentResponse:
    student = students.get(student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

# Update a student
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_update: StudentCreate, student_id: int = Path(..., gt=0)) -> StudentResponse:
    existing_student = students.get(student_id)
    if existing_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    updated_student = StudentResponse(id=student_id, **student_update.model_dump())
    students[student_id] = updated_student
    return updated_student

# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int = Path(..., gt=0)
                   ) -> dict[str, str]:
    if student_id not in students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    del students[student_id]
    return {"message": "Student deleted successfully"}