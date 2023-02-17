from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from dbnew import DB
from BaseModels_gncorp import Employee, Teams

app = FastAPI()
db = DB("GNCorp.db")

@app.get ("/")
def root():
    return "Welcome to employees database"
# Base no longer needed since i have another one that takes both id and by their first name
# @app.get("/employees/{id}")
# def get_employee_by_id(id: int):
#     emp = db.get_tables(table="employees", where=("id", str(id)))
#     return emp
# Base
@app.get("/teams/{id}")
def get_team_by_id(id: int):
    tm = db.get_tables(table="teams", where=("id", str(id)))
    return tm

@app.get("/employees/{id_title}")
def get_person_by_id(id_title: int | str):
        if type(id_title) is int:
                data = db.get_tables(table="employees", where=("id", str(id_title) ))
        if type(id_title)is str:
                data = db.get_tables(table="employees", where=("first_name", id_title))
        return data 



@app.get("/employee/{first_name}")
def get_employee_by_name(first_name:str):
    emp = db.get_tables(table="employees", where=("first_name", first_name))
    return emp



@app.get("/employees_details")
def get_employees():
        data = db.get_employee_details()
        return data

@app.get("/teams_details")
def get_teams():
        data = db.get_team_details()
        return data
     
 
@app.post("/add_employee")
def create_employee(employee: Employee):
        print(employee)
        db.insert_tables(table="employees", 
                fields={"first_name":employee.first_name, 
                      "last_name": employee.last_name,
                      "team_id": str(employee.team_id), 
                      "leader_id": str(employee.leader_id), 
                      "title": employee.title,
                      "description": employee.description}
        )
        return "Added the new employee"

@app.post("/add_team")
def create_employee(teams: Teams):
        print(teams)
        db.insert_tables(table="teams", 
                fields={"team_name":teams.team_name,
                      "leader_id": str(teams.leader_id), 
                      "description": teams.description}
        )
        return "Added the new team"
    

@app.put("/update_employee/{id}")
def update(id:int, employee: Employee ):
        db.update_tables(table="employees", 
                fields={"first_name":employee.first_name, 
                "last_name": employee.last_name, 
                "title": employee.title,
                "description": employee.description},
                where=("id", str(id)),
        )
        return "updated employee"

@app.put("/update_teams/{id}")
def update(id:int,team: Teams ):
        db.update_tables(table="teams", 
                fields={"team_name": team.team_name,
                        "description": team.description},
                where=("id", str(id)),
        )
        return "updated team"


@app.delete("/remove_employee/{id}")
def delete_employee(id):
        db.delete_row(table="employees", id=id)
        return "remove complete"

#WIP for later experiment
@app.get("/emp/{id_title}")
def get_person_by_id(id_title: int | str):
        if type(id_title) is int:
                data = db.get_emp_test(table="employees", where=("id", str(id_title) ))
        if type(id_title)is str:
                data = db.get_emp_test(table="employees", where=("first_name", id_title))
        return data 
#for later experiments
@app.get("/tables")
def get_tables():
        emp = db.get_tables(table="employees")
        teams = db.get_tables(table="teams")
        return emp, teams

