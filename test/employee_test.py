from typing import List
import requests

from employees_models import Employee, Teams



def url(route: str):
    return f"http://127.0.0.1:8000{route}"

print("Welcome to the employee database")

def print_menu_list():
    print(
        """
        1: Add Employeee
        2: See the employees
        3: Remove employee
        4: Update employee
        5: See the teams
        6: Exit program
        """
    )
    pass

def add_employee():
    print("Add Employee")
    first_name = input("Employees first name: ")
    last_name = input("Employees last name: ")
    title = input("Employee title: ")
    leader_id = input("Leader id: ")
    team_id = input("Team id: ")
    description = input("Employee description: ")
    new_employee = Employee(first_name=first_name,last_name=last_name,leader_id=leader_id,team_id=team_id, title=title, description=description)
    res = requests.post(url("/add_employee"), json=new_employee.dict())
    print(res)


def get_employee():
    employees = []
    print("See the employees")
    res = requests.get(url("/employees"))
    if not res.status_code == 200:
        return
    data = res.json()
    for employee in data:  
        employee = Employee (**employee) # Problem here 
        print("__________")
        print(f"Employee ID: {employee.id}")
        print(f"First name: {employee.first_name}")
        print(f"Last name: {employee.last_name}")
        print(f"Leader ID: {employee.leader_id}")
        print(f"Team ID: {employee.team_id}")
        print(f"Title: {employee.title}")
        print(f"Details: {employee.description}")
        employees.append(employee)
    return employees


def remove_employee():
    print("__________")
    print("Remove Employee")
    todo_to_delete = input("Employee you wish to remove please enter the ID: ")
    if not str.isdigit(todo_to_delete):
        print("__________")
        print("Please user the ID number of the employee")
        return
    res = requests.delete(url(f"/remove_employee/{todo_to_delete}"))
    print(res.json())


def update_employee(employees: List[Employee]):
    print("__________")
    print("Update employee", employees)
    
    employee_to_update = input("Enter employee ID you wish to update: ")
    if not str.isdigit(employee_to_update):
        print("__________")
        print("Please enter the employee ID number ")
        return

    index = None
    for i, employee in enumerate(employees):
        print(employee.id)
        if employee.id == int(employee_to_update):
            index = i
            break

    if index == None:
        print("__________")
        print("No such ID, please enter correct ID number")
        return
    employee = employees[index]

    #if i want update the whole employee 
    first_name = input("Employee first name (leave blank if same): ")
    last_name = input("Employee last name (Leave blank if same): ")
    title = input("Employee title (leave blank if same): ")
    description = input("Employee description (Leave blank if same): ")
    
    #if i only want to change the title and description
    #first_name = employee.first_name
    #last_name = employee.last_name
    
    #if i want to update the whole employee id 
    if not first_name:
         first_name = employee.first_name
    
    if not last_name:
         last_name = employee.last_name

    if not title:
        title = employee.title
    if not description:
        description = employee.description
    
    new_update = Employee(first_name=first_name, last_name=last_name,title=title, description=description)
    res = requests.put(url(f"/update_employee/{employee_to_update}"), json=new_update.dict())
    print(res.json())
    
    
def get_teams():
    teams = []
    print("See the teams")
    res = requests.get(url("/teams"))
    if not res.status_code == 200:
        return
    data = res.json()
    for team in data:  
        team = Teams(**team) 
        print("__________")
        print(f"Team ID: {team.team_id}")
        print(f"Team name: {team.team_name}")
        print(f"Employee(leader) id: {team.leader_id}")
        teams.append(team)
    return teams

def get_both():
    both= []
    print("See the teams")
    res = requests.get(url("/teams_employees"))
    if not res.status_code == 200:
        return
    data = res.json()
    for boths in data:  
        boths = Teams(**both) 
        print("__________")
        print(f"Team ID: {boths.team_id}")
        print(f"Team name: {boths.team_name}")
        print(f"Employee(leader) id: {boths.leader_id}")
        both.append(both)
    return both

# not finished to add to team probably unccesary 
def add_team():
    print("Add to Team")
    team_id = team_id
    leader_id = leader_id
    team_name = team_name
    new_employee = Teams(team_id=team_id, leader_id=leader_id, team_name=team_name)
    res = requests.put(url("/add_employee"), json=new_employee.dict())
    print(res)


def main():
    print("__________________________")
    print_menu_list()
    choice = input("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("__________________________")
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            add_employee()
        case 2:
            employees = get_employee()
        case 3:
            remove_employee()
        case 4:
            employees = get_employee()
            update_employee(employees)
        case 5:
            teams = get_teams()
        case 6:
            exit()
        case _:
            print("Please enter a valid choice")


while __name__ == "__main__":
    main()
    