from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    city: str


@app.get("/")
def home():
    return {
        "message": "Welcome to NeuroMind AI!"
    }


@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student Created Successfully",
        "student": student
    }


@app.get("/about")
def about():
    return {
        "project": "NeuroMind AI",
        "version": "1.0",
        "developer": "Pratiksha"
    }