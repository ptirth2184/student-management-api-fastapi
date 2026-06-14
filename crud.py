from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate

# Create a new student
def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        age=student.age,
        course=student.course,
        email=student.email
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


#get all students
def get_students(db: Session):
    return db.query(Student).all()

#get student by id
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


# Search students by course
def search_students_by_course(db: Session, course: str):
    return db.query(Student).filter(Student.course.ilike(f"%{course}%")).all()


# Update an existing student
def update_student(db: Session, student):
    db_student = db.query(Student).filter(Student.id == student.id).first()
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.course = student.course
        db_student.email = student.email
        db.commit()
        db.refresh(db_student)
    return db_student


# Delete a student
def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student