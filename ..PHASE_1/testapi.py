# -*- coding: utf-8 -*-
"""

@author: Musab Baloch

"""

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# GET
# POST
# PUT
# DELETE

class Student(BaseModel):
    name: str
    age: int
    semester: int
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    semester: Optional[int] = None
    

students = {
    
    3012345 : {
        "name" : "Ali",
        "age" : 20,
        "semester" : 3
        },
    
    3067891 :  {
        "name" : "Abdullah",
        "age" : 20,
        "semester" : 2
        },
    
    3061798 :  {
        "name" : "Taimoor",
        "age" : 21,
        "semester" : 2
        }
    }

@app.get("/")
def root():
    return {"status" : "Successful Hermano"}

@app.get("/get-student_info_id/{id}")
def send_info_id(id : int = Path(..., description="The ID Code of the Student", ge=3000000)):
    if id in students:
        return students[id]
    return {"Status" : "Data not found"}

@app.get("/get-student_info_name/{name}")
def send_info_name(name : str):
    for id,data in students.items():
        if name not in data.values():
            continue
        else:
            return students[id]
    return {"Status" : "Data not found"}

@app.delete("/delete-account/{student_id}")
def delete_acct(student_id: int):
    if student_id not in students:
        return {"Error" : "Student not found"}
    
    students.pop(student_id)
    return {"Status" : "Account deletion successful"}

@app.post("/create-account/{student_id}")
def create_acct(student_id: int, student : Student):
    if student_id in students:
        return {"ERROR" : "Student already exists."}
    students[student_id] = student
    return {"Status" : "Account creation successful"}


@app.put("/update-account/{student_id}")
def update_acct(student_id: int, student : UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student not found"}
    
    if student.name != None:
        students[student_id]["name"] = student.name
        
    if student.age != None:
        students[student_id]["age"] = student.age
        
    if student.semester != None:
        students[student_id]["semester"] = student.semester
        
    return {"Status" : "Account updated successfully"}


    
        


