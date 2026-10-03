import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI, Depends, HTTPException

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def check_database_connection():
    try:
        # Attempt to connect to the database
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
    return True
check_database_connection()

app = FastAPI(title="neon db test", description="postgres sql", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Welcome to my home page"}

# @app.get("/students")
# def get_students_data():
#     try:
#         with SessionLocal() as session:
#             result = session.execute(text("SELECT * FROM students"))
#             # students = result.fetchall()
#         # return students
#         # return [dict(row) for row in result.mappings().all()]

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error fetching students data: {e}")

@app.get("/students")
def get_students_data():
    try:
        with SessionLocal() as session:
            result = session.execute(text("SELECT * FROM students"))
            students = result.mappings().all()
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching students data: {e}")

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    try:
        with SessionLocal() as session:
            result = session.execute(
                text("SELECT * FROM students WHERE id = :id"),
                {"id": student_id}
            )
            student = result.mappings().first()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        return student
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching student data: {e}"
        )



from pydantic import BaseModel ,Field , EmailStr, HttpUrl, field_validator   
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=100)
    city: str = Field(min_length=2, max_length=50)
@app.post("/students_create")
def create_student(student: StudentCreate):
    try:
        with SessionLocal() as session:
            session.execute(
                text("INSERT INTO students (name, age, city) VALUES (:name, :age, :city)"),
                {"name": student.name, "age": student.age, "city": student.city}
            )
            session.commit()
        return {"message": "Student created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating student: {e}")

@app.put("/students_update/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    try:
        with SessionLocal() as session:
            session.execute(
                text("UPDATE students SET name = :name, age = :age, city = :city WHERE id = :id"),
                {
                    "name": student.name,
                    "age": student.age,
                    "city": student.city,
                    "id": student_id
                }
            )
            session.commit()
        return {"message": "Student updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error updating student: {e}"
        )
    
@app.patch("/students_patch/{student_id}")
class studentpatch(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    age: int | None = Field(default=None, ge=0, le=100)
    city: str | None = Field(default=None, min_length=2, max_length=50)
def patch_student(student_id: int, student: studentpatch):
    try:
        with SessionLocal() as session:
            update_data = {
                k: v for k, v in student.dict().items() if v is not None
            }
            if update_data:
                set_clause = ", ".join(
                    [f"{k} = :{k}" for k in update_data.keys()]
                )
                update_data["id"] = student_id
                session.execute(
                    text(f"UPDATE students SET {set_clause} WHERE id = :id"),
                    update_data
                )
                session.commit()
        return {"message": "Student patched successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error patching student: {e}"
        )

@app.delete("/students_delete/{student_id}")
def delete_student(student_id: int):
    try:
        with SessionLocal() as session:
            session.execute(
                text("DELETE FROM students WHERE id = :id"),
                {"id": student_id}
            )
            session.commit()
        return {"message": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting student: {e}")