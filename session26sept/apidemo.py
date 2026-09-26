from fastapi import FastAPI
app = FastAPI()


@app.get("/sudh")
def test():
    return {"message": "Hello, World!"}

@app.get("/euron")
def euron_details():
    return{"message": "Euron Details"}

@app.get("/sudhanshu")
def euron_details():
    return{"message": "Sudhanshu Details"}

@app.get("/course/{course_name}")
def get_course_detials(course_name:str)->dict:
    #https://fbc3-223-181-112-66.ngrok-free.app/course/python'
    return {"message": f"Details for course {course_name}"}

@app.get("/student1s")
def student_search(student_id:int):
    #https://fbc3-223-181-112-66.ngrok-free.app/student?student_id=3
    return {"student_id": student_id} 


@app.get("/mentor")
def get_mentor(mentor_id:int | None=None):
    #https://fbc3-223-181-112-66.ngrok-free.app/docs#/default/get_mentor_mentor_get
    return {"mentor_id": mentor_id} 


from pydantic import BaseModel, Field, EmailStr, HttpUrl
class Student(BaseModel):
    student_id:int =Field(ge=0, le=1000)
    student_name: str =Field(min_length=5, max_length=50)


# @app.post("/student")
# def create_student(student_id:int, student_name: str):
#     return {"student_id", student_id, "student_name", student_name}


@app.post("/student")
def create_student(student:Student):
    return {"student_id", student.student_id, "student_name", student.student_name}