from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from employee_test import Employee
from employee_test import Teams
from db_test import DB
#from db1 import DB


app = FastAPI()
db = DB("GNCorp.db")
#db = DB("teams.db")
#db = DB()

app.curr_id = 1
#app.employees: List[Employee] = []
app.team_id = 1
#app.teams: List[Teams]


@app.get ("/")
def root():
    return "Welcome to employees database"

@app.get("/employees")
def get_employee():
    get_employee_query = """
    SELECT * FROM employees 
    """
    data = db.call_db(get_employee_query)
    employees = []
    for element in data:
        id, first_name, last_name,team_id, leader_id, title, description = element
        employees.append(Employee( id=id, first_name=first_name, last_name=last_name,team_id=team_id,leader_id=leader_id, title=title, description=description))
    print(data)
    return employees

@app.get("/teams")
def get_team():
    get_team_query = """
    SELECT * FROM teams
    """
    data = db.call_db(get_team_query)
    teams = []
    for element in data:
        team_id, leader_id, team_name = element
        teams.append(Teams(team_id=team_id,leader_id=leader_id, team_name=team_name))
    print (data)
    return teams  

@app.post("/add_employee")
def add_employee(employee: Employee):
    insert_query = """
    INSERT INTO employees(first_name, last_name, leader_id, team_id, title, description)
    VALUES (?,?,?,?,?,?)
    """
    db.call_db(insert_query, employee.first_name, employee.last_name, employee.leader_id, employee.team_id,employee.title, employee.description)
    return "Adds a employee"

@app.put("/update_employee/{id}")
def update_employee(id: int, update: Employee):
    update_employee_query ="""
    UPDATE employees
    SET first_name = ?, last_name = ?,title = ?, description = ?
    WHERE id = ?;
    """
    db.call_db(update_employee_query, update.first_name, update.last_name, update.title, update.description, id)
    return True

@app.post("/add_team/")
def add_team(teams: Teams):
    insert_team_query ="""
    INSERT INTO teams(team_name, leader_id)
    VALUES (?,?)
    """
    db.call_db(insert_team_query, teams.team_name, teams.leader_id)
    return "Adds a team"

@app.delete("/remove_employee/{id}")
#def remove_employee(id: int, leader_id: int)
def remove_employee(id: int):
    remove_query ="""
    DELETE FROM employees WHERE id = ?
    """
    # remove_team ="""
    # DELETE FROM employees WHERE leader_id = ?
    # """ 
    
    db.call_db(remove_query, id)
    #db.call_db(remove_team, leader_id)
    return True


@app.get("/teams_employees")
def get_both():
    get_both_query = """
    SELECT * FROM employees
    WHERE id = team_id,
    """
    both = []
    data = db.call_db(get_both_query)
    for elements in data:
            id = elements
            both.append(Teams(id=id))
    print(data)
    return "Both teams"
    
    