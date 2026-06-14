from fastapi import Depends, FastAPI, HTTPException, status, Path
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from schemas import StudentCreate, StudentResponse
import crud
from pydantic import BaseModel, Field
from typing import List


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student Management API")

# connect to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)) -> StudentResponse:
    return crud.create_student(db=db, student=student)
    return new_student

# Search students by course
@app.get("/students/search", response_model=List[StudentResponse])
def search_students(course: str) -> List[StudentResponse]:
    return [student for student in students.values() if course.lower() in student.course.lower()]


# Get all students
@app.get("/students", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)) -> List[StudentResponse]:
    return crud.get_students(db=db)

# Get a student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int = Path(..., gt=0), db: Session = Depends(get_db)) -> StudentResponse:
    student = crud.get_student(db=db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

# Update a student
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_update: StudentCreate, student_id: int = Path(..., gt=0), db: Session = Depends(get_db)) -> StudentResponse:
    existing_student = crud.get_student(db=db, student_id=student_id)
    if existing_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    updated_student = StudentResponse(id=student_id, **student_update.model_dump())
    crud.update_student(db=db, student=updated_student)
    return updated_student

# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    if not crud.get_student(db=db, student_id=student_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    crud.delete_student(db=db, student_id=student_id)
    return {"message": "Student deleted successfully"}