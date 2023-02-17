import sqlite3
import os
from typing import Dict, Tuple
from BaseModels_gncorp import Employee, Teams

class DB:
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url
        if not os.path.exists(self.db_url):
            self.set_up_db()

    def set_up_db(self):
        conn = sqlite3.connect(self.db_url)
        with open("gn_setup.sql", "r") as file:
            script = file.read()
            conn.executescript(script)
            conn.commit()

        conn.close()

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data
    
    def insert_tables(self, *, table: str, fields: Dict[str, str]):
        keys = ",".join(fields.keys())
        values = "','".join(fields.values())

        query = f"""
        INSERT INTO {table} (
            {keys}
        ) VALUES (
            '{values}'
        )
        """
        return self.call_db(query)
    
    def get_tables(self, *, table: str, where: Tuple[str, str] | None = None):
        query = f"""
        SELECT * FROM {table} 
        """
        if where:
            keys, values = where
            where_query = f"""
            WHERE {keys} = '{values}'
            """
            query = query + where_query
        data = self.call_db(query)
        return data
    
    def get_employee_details(self):
        get_employee_query = """
        SELECT * FROM employees 
        """
        data = self.call_db(get_employee_query)
        employees = []
        for element in data:
            id, first_name, last_name, leader_id, team_id, title, description = element
            employees.append(Employee( id=id, first_name=first_name, last_name=last_name, leader_id=leader_id, team_id=team_id, title=title, description=description))
        print(data)
        return employees
    
    def get_team_details(self):
        get_team_query = """
        SELECT * FROM teams
        """
        data = self.call_db(get_team_query)
        teams = []
        for element in data:
            id, team_name, leader_id, description = element
            teams.append(Teams(id=id,team_name=team_name, leader_id=leader_id,description=description))
        print (data)
        return teams  
    
    def delete_row(self, *, table: str, id: int):
        delete_query = f"""
        DELETE FROM {table} WHERE id = {id}
        """
        self.call_db(delete_query)

    def update_tables(self, *, table: str, where: Tuple[str, str], fields: Dict[str, str]):
        where_key, where_val = where
        field_query = ""
        for key, val in fields.items():
            field_query += f"{key} = '{val}',"
        field_query = field_query[:-1]
        update_query = f"""
        UPDATE {table} SET {field_query} WHERE {where_key} = '{where_val}' 
        """
        print(update_query)
        data = self.call_db(update_query)
        return data
        
 
# TEST CODES and CONCEPTS
    
    def get_emp_test(self, * , table:str, where: Tuple[str,str]|None=None):
        get_employee_query = f"""
        SELECT * FROM {table} 
        """
        
        if where:
            keys, values = where
            where_query =f"""
            WHERE {keys} = '{values}'
            """
            get_employee_query = get_employee_query + where_query
        
        emp = self.call_db(get_employee_query)
        employees = []
        for employee in emp:
            id, first_name, last_name, leader_id, team_id, title, description = employee
            employees.append(Employee( id=id, first_name=first_name, last_name=last_name, leader_id=leader_id, team_id=team_id, title=title, description=description))
        print(emp)
        return employees