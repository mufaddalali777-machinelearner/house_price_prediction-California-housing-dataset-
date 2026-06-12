from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#this is an instance or object of class FastAPI that we have created and given it the name app
#now we will create an endpoint
#an endpoint is one endpoint of an communication channel

# eg: amazon.com/create-user
#Types of endpoints:
#GET : GET AN INFORMATION
#POST - CREATE SOMETHING NEW
#PUT - UPDATE
#DELETE - DELETE SOMETHING

@app.get("/")
def index():
    return {"name": "First Data"}

# go to command prompt and run this saying:python -m uvicorn myapi:app --reload
# it will give me an web link: https.....
##http://127.0.0.1:8000

#END POINT PARAMETERS

students = {1:{"name" : "Mufaddal", "age" : "20", "year" : "Btech 3rd"}}



class Student(BaseModel):
    name : str
    age : int
    year : str

class Updatestud (BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

@app.get("/get-student/{stud_id}")
def student_id(stud_id : int = Path(..., description="Enter your fucking id you mf", gt = 0, lt = 4)):
    return students[stud_id]

#query parameter
@app.get("/get-by-name/{student_id}")
def ger_student(*, student_id :int, name : str = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"}
# in the above for multiple parameter, we should ensure that optional parameter should not occur before the required parameters, 
#if it happens so, then we should place the req param first,then the optional
#but if we want to pass in any order,then we will have to use the *, first 


# combining path and query parameter

#request body and the post method
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student ):
    if student_id in students:
        return {"Error" : "Student exists"}
    students[student_id] = student
    return students[student_id]

#put method
@app.put("/updates-student/{student_id}")
#but now if we use the same Student class, we will have to change everything for it to be updated, and that is not a good practise as we have to update only some, not all info
# so we create a new class and then use optional for each(line)
def update_student(student_id : int, student : Updatestud):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id]

#delete method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    del students[student_id]
    return {"Message" : "Student deleted successfully"}