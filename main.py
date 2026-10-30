
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float = Field(ge=0, le=100)


@app.post("/students")
def add_student(student: Student):
    for s in students:
        if s["id"] == student.id:
            raise HTTPException(400, "Student already exists")
    students.append(student.model_dump())
    return {"message": "Student added"}


@app.get("/students")
def get_students(course: Optional[str] = None):
    if course:
        return [s for s in students if s["course"].lower() == course.lower()]
    return students


@app.get("/students/{id}")
def get_student(id: int):
    for s in students:
        if s["id"] == id:
            return s
    raise HTTPException(404, "Student not found")


@app.put("/students/{id}")
def update_student(id: int, student: Student):
    for i, s in enumerate(students):
        if s["id"] == id:
            students[i] = student.model_dump()
            return {"message": "Student updated"}
    raise HTTPException(404, "Student not found")


@app.delete("/students/{id}")
def delete_student(id: int):
    for s in students:
        if s["id"] == id:
            students.remove(s)
            return {"message": "Student deleted"}
    raise HTTPException(404, "Student not found")

@app.get("/students")
def get_students(course: Optional[str] = None):
    if course:
        return [s for s in students if s["course"].lower() == course.lower()]
    return students