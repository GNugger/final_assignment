from typing import List, Dict
import requests
from BaseModels_gncorp import Employee, Teams
from IPython.utils import io

def url(route: str):
    return f"http://127.0.0.1:8000{route}"

print("Welcome to the employee database")

def print_menu_list():
    print(
        """
        1: Add team or employee
        2: Search teams/employees by ID
        3: Remove employee
        4: Update employee
        5: See list of teams/employees
        6: Search employees by first name
        7: Exit program
        """
    )
    pass


# create a new employee or team in the table
def add_new_row():
    print("__________")
    choice = input("Add new team[1] or employee[2]: ")
    choice = choice.strip()
    
    if not str.isdigit(choice):
        print("__________________________")
        print("Please enter a number")
        return
    
    match int(choice):
        case 1:
            print("Add team")
            team_name = input("Team name:  ")
            leader_id = input("Leader id: ")
            description = input("Team description: ")
            new_team = Teams(team_name=team_name, leader_id=leader_id,description=description)
            res = requests.post(url("/add_team"), json=new_team.dict())
            print(res)
            return 
            
        case 2:
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
            return 
            

# to make the tables have more details/description on them
def get_emp_details():
    employees = []
    print("Employee details")
    res = requests.get(url("/employees_details"))
    if not res.status_code == 200:
        return
    data = res.json()
    for employee in data:  
        employee = Employee(**employee)
        print("__________")
        print(f"Employee ID: {employee.id}")
        print(f"First name: {employee.first_name}")
        print(f"Last name: {employee.last_name}")
        print(f"Title: {employee.title}")
        print(f"Details: {employee.description}")
        employees.append(employee)
    return employees

def get_teams_details():
    teams = []
    print("Teams details")
    res = requests.get(url("/teams_details"))
    if not res.status_code == 200:
        return
    data = res.json()
    for team in data:  
        team = Teams(**team) 
        print("__________")
        print(f"Team ID: {team.id}")
        print(f"Team name: {team.team_name}")
        print(f"Employee(leader) id: {team.leader_id}")
        print(f"Description: {team.description}")
        teams.append(team)
    return teams

# can make it with remove team to but rarely that is need or desired since teams are just teams in my logic compare to employees that comes and goes
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


#new update with options  
def update_tables(details_team=List[Teams], details_employees=List[Employee] ):
    print("__________________________")
    choice=input("Choose teams[1] or employees[2] to update: ")
    choice = choice.strip()        
    if not str.isdigit(choice):
        print("__________________________")
        print("Please enter the number ")
        return
    
    match int(choice):
        case 1:
       
            team_to_update = input("Enter team ID you wish to update: ")
            if not str.isdigit(team_to_update):
                print("__________")
                print("Please enter the team ID number ")
                return

            index = None
            for i, team in enumerate(details_team):
                if team.id == int(team_to_update):
                    index = i
                    break

            if index == None:
                print("__________")
                print("No such team ID, please enter correct ID number")
                return
        
            team = details_team[index]
            
            team_name = input("Team name (leave blank if same): ")
            description = input("Team description (Leave blank if same): ")

            if not team_name:
                team_name = team.team_name
                
            if not description:
                description = team.description
        
            new_update = Teams(team_name=team_name, description=description)
            res = requests.put(url(f"/update_teams/{team_to_update}"), json=new_update.dict())
            print(res.json())
            
        
        case 2:
            
            employee_to_update = input("Enter employee ID you wish to update: ")
            if not str.isdigit(employee_to_update):
                print("__________")
                print("Please enter the employee ID number ")
                return

            index = None
            for i, employee in enumerate(details_employees):
                if employee.id == int(employee_to_update):
                    index = i
                    break

            if index == None:
                print("__________")
                print("No such employee ID, please enter correct ID number")
                return
        
            employee = details_employees[index]
            
            first_name = input("Employee first name (leave blank if same): ")
            last_name = input("Employee last name (Leave blank if same): ")
            title = input("Employee title (leave blank if same): ")
            description = input("Employee description (Leave blank if same): ")
            
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
        
        case _:
            print("""
                  please enter the correct number
                  now going back to main menu
                  
                  """)


# OK
def serach_in_tables(teamlist = List[Teams], emplist = List[Employee]):
    print("__________________________")
    select = input("Select which table you want to search [1] for teams or [2] for employees: ")
    select = select.strip() 
    
    if not str.isdigit(select):
        print("__________________________")
        print("Please enter a number")
        return
    
    match int(select):
        case 1:
            tm_to_show = input("Enter Team ID you wish to show: ")
            if not str.isdigit(tm_to_show):
                print("__________")
                print("Please enter the Team ID number ")
                return
            
            index = None
            for i, tm in enumerate(teamlist):
                if tm.id == int(tm_to_show):
                    index = i
                    break

            if index == None:
                print("__________")
                print("No such Team ID, please enter correct ID number")
                return
            
            tm = teamlist[index]
            
            
            res = requests.get(url(f"/teams/{tm_to_show}"))
            print("'ID', 'Team Name', 'Leader ID', 'Description'")
            print(res.json())
            if not res.status_code == 200:
                return
            return tm
            
        case 2:
            
            emp_to_show = input("Enter employee ID you wish to show: ")
            if not str.isdigit(emp_to_show):
                print("__________")
                print("Please enter the employee ID number ")
                return
            
            index = None
            for i, emp in enumerate(emplist):
                if emp.id == int(emp_to_show):
                    index = i
                    break

            if index == None:
                print("__________")
                print("No such employee ID, please enter correct ID number")
                return
            
            emp = emplist[index]
            
            
            res = requests.get(url(f"/employees/{emp_to_show}"))
            print("'ID', 'First Name', 'Last Name', 'Team ID', 'Leader ID', Title', 'Description'")
            print(res.json())
            if not res.status_code == 200:
                return
            return emp
        case _:
            pass

#Able to searach employees by their first name           
def get_first_name():
    first_name = input("Enter employees first name: ")
    first_name = first_name.capitalize()
    res = requests.get(url(f"/employees/{first_name}"))
    if not res.status_code == 200:
        return
    data = res.json()
    for tables in data:
        print("__________")
        print("'ID', 'First Name', 'Last Name', 'Team ID', 'Leader ID', Title', 'Description'")
        print(tables)
    return tables

## Not in use because it just prints everything but is there in case i want to do that            
# def get_tables():
#     res = requests.get(url("/tables"))
#     if not res.status_code == 200:
#         return
#     data = res.json()
#     for tables in data:
#         print("__________")
#         print(tables)
#     return tables

#WIP for later experiment
# def get_emp_first_name():
#     employees = []
#     first_name = input("Enter employees first name: ")
#     res = requests.get(url(f"/emp/{first_name}"))
#     if not res.status_code == 200:
#         return
#     data = res.json()
#     for employee in data:  
#         employee = Employee(**employee)
#         print("__________")
#         print(f"Employee ID: {employee.id}")
#         print(f"First name: {employee.first_name}")
#         print(f"Last name: {employee.last_name}")
#         print(f"Title: {employee.title}")
#         print(f"Details: {employee.description}")
#         employees.append(employee)
#     return employees

        
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
            add_new_row()
        case 2:
            # serach by id OK, found IPython libary to prevent printing the function i need
            with io.capture_output():
                tm = get_teams_details()
                emp = get_emp_details()
            serach_in_tables(tm,emp)
            
        case 3:
            remove_employee()
        case 4:
            
            with io.capture_output():
                teams = get_teams_details()
                employees = get_emp_details()
            
            print("__________")
            update_tables(teams,employees)
            
        case 5:
            select = input("Select 1 for teams details or 2 for employees or 3 for both list: ")
            select = select.strip()
            if not str.isdigit(select):
                print("__________________________")
                print("Please enter a valid option")
                return
            
            match int(select):
                    case 1:
                        get_teams_details()
                    case 2:    
                        get_emp_details()
                    case 3:
                        print("__________________________")
                        get_emp_details()
                        print("__________________________")
                        get_teams_details()
        case 6:
            get_first_name()
            #WIP
            #get_emp_first_name()
                      
        case 7:
            exit()
        case _:
            print("Please enter a valid choice")


while __name__ == "__main__":
    main()
    