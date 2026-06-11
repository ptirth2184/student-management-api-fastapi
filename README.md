# Student Management API

A RESTful Student Management API built with FastAPI to demonstrate CRUD operations, request validation, response modeling, and REST API best practices.

## Features

### Student Operations

* Create Student
* Get All Students
* Get Student By ID
* Update Student
* Delete Student
* Search Students By Course

### API Features

* Request Validation with Pydantic
* Response Models
* Path & Query Parameters
* Proper HTTP Status Codes
* Exception Handling
* Interactive API Documentation (Swagger UI & ReDoc)

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
student-management-api-fastapi/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ptirth2184/student-management-api-fastapi.git
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

FastAPI automatically generates interactive API documentation.

Once the server is running, visit:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Swagger UI Preview

```markdown
![Swagger UI](https://raw.githubusercontent.com/ptirth2184/student-management-api-fastapi/main/screenshots/swagger-ui.png)
```

## API Endpoints

| Method | Endpoint                     | Description               |
| ------ | ---------------------------- | ------------------------- |
| POST   | `/students`                  | Create a student          |
| GET    | `/students`                  | Retrieve all students     |
| GET    | `/students/{student_id}`     | Retrieve a student by ID  |
| PUT    | `/students/{student_id}`     | Update a student          |
| DELETE | `/students/{student_id}`     | Delete a student          |
| GET    | `/students/search?course=AI` | Search students by course |

## Sample Request

### Create Student

**POST** `/students`

```json
{
  "name": "Tirth Patel",
  "age": 21,
  "course": "AI & DS",
  "email": "tirth@example.com"
}
```

## Sample Response

```json
{
  "id": 1,
  "name": "Tirth Patel",
  "age": 21,
  "course": "AI & DS",
  "email": "tirth@example.com"
}
```

## Sample Error Response

```json
{
  "detail": "Student not found"
}
```

## Future Improvements

* Database Integration with SQLAlchemy
* PostgreSQL Integration
* JWT Authentication
* Docker Containerization
* Pagination
* Unit & Integration Testing
* Cloud Deployment
* Role-Based Access Control (RBAC)

## Learning Outcomes

This project helped me understand:

* FastAPI fundamentals
* CRUD API design
* Request and Response Models
* Data Validation with Pydantic
* Path and Query Parameters
* HTTP Status Codes
* Exception Handling
* REST API Best Practices

## Author

**Tirth Patel**

Aspiring AI/ML Engineer and Backend Developer, currently learning FastAPI and building production-ready backend systems.
