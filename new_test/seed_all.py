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

with open("seed_all.json", "r") as seed:
    data = json.load(seed)

    for emp in data["employees"]:
        db.call_db(create_employees, 
                   emp["first_name"],
                   emp["last_name"],
                   emp["team_id"],
                   emp["leader_id"],
                   emp["title"],
                   emp["description"])

    for team in data["teams"]:
        db.call_db(create_team,
                   team["team_name"],
                   team["leader_id"],
                   team["description"])


print(emp)
print(team)