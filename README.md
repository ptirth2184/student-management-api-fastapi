# Student Management API

A RESTful Student Management API built with FastAPI as part of my backend engineering learning journey.

## Features

- Create Student
- Get All Students
- Get Student By ID
- Update Student
- Delete Student
- Search Students By Course
- Request Validation with Pydantic
- Response Models
- Proper HTTP Status Codes
- Exception Handling

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
main.py
requirements.txt
README.md
```

## Installation

Clone the repository:

```bash
git clone <repo-url>
cd student-management-api-fastapi
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

## API Documentation

FastAPI automatically generates interactive documentation:

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /students | Create a student |
| GET | /students | Get all students |
| GET | /students/{id} | Get a student by ID |
| PUT | /students/{id} | Update a student |
| DELETE | /students/{id} | Delete a student |
| GET | /students/search | Search students by course |

## Sample Request

POST /students

```json
{
  "name": "Tirth Patel",
  "age": 21,
  "course": "AI & DS",
  "email": "tirth@example.com"
}
```

## Future Improvements

- Database Integration with SQLAlchemy
- Authentication & Authorization
- Pagination
- Docker Support
- Unit Testing
- Deployment

## Learning Outcomes

This project helped me understand:

- FastAPI fundamentals
- Request and response models
- CRUD API design
- Data validation with Pydantic
- REST API best practices