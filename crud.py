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