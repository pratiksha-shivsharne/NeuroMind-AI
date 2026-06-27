from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Student(BaseModel):
    name: str
    city: str

@app.get("/")

@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student Created Successfully",
        "student": student
    }

def home():
    return {
        "message": "Welcome to NeuroMind AI!"
    }

@app.get("/about")
def about():
    return {
        "project": "NeuroMind AI",
        "version": "1.0",
        "developer": "Pratiksha"
    }