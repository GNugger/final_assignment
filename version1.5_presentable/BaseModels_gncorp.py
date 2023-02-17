from pydantic import BaseModel

# Standard BaseModels 

class Employee(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    team_id: int = None
    leader_id: int = None
    title: str
    description: str
    #full_name = first_name + " " + last_name #ska testas för att skriva ut hela namnet 
    
class Teams(BaseModel):
    id: int = None
    team_name: str
    leader_id: int = None
    description: str