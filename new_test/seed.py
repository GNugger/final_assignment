import json
from dbnew import DB

db = DB("GNCorp.db")

create_employees = """
INSERT INTO employees (
    first_name,
    last_name,
    team_id,
    leader_id,
    title, 
    description
    ) 
VALUES (?, ?, ? ,? ,? ,?)
"""
create_team ="""
INSERT INTO teams (
    team_name,
    leader_id,
    description
)
VALUES (?, ?, ?)
"""

with open("seed_emp.json", "r") as employees:
    data = json.load(employees)

    for emp in data:
        db.call_db(create_employees, 
                   emp["first_name"],
                   emp["last_name"],
                   emp["team_id"],
                   emp["leader_id"],
                   emp["title"],
                   emp["description"])

with open ("seed_team.json", "r") as teams:
    data = json.load(teams)
    for team in data:
        db.call_db(create_team,
                   team["team_name"],
                   team["leader_id"],
                   team["description"])


print(emp)
print(team)