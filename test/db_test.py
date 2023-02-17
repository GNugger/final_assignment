import sqlite3
import os


class DB:
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url

        if not os.path.exists(self.db_url):
            self.init_db()

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, args,)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data
    
   

    def init_db(self):
        init_employee_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            leader_id INTEGER,
            team_id INTEGER,
            title TEXT NOT NULL,
            description TEXT NOT NULL
            );
        """
        init_teams_query = """
        CREATE TABLE IF NOT EXISTS teams(
            team_id INTEGER PRIMARY KEY,
            leader_id INTEGER,
            team_name TEXT NOT NULL,
            FOREIGN KEY(leader_id) REFERENCES employees(id) 
        )
        """
        
        
        insert_employee_query = """
        INSERT INTO employees (first_name, last_name,leader_id, team_id,title, description)
        VALUES ('GN','Drive',1, 1, 'CEO','Owner');
        """
        insert_teams_query = """
        INSERT INTO teams (team_name, leader_id)
        VALUES ('Celestial Being',1);
        """
        
        
        self.call_db(init_employee_query)
        self.call_db(insert_employee_query)
        self.call_db(init_teams_query)
        self.call_db(insert_teams_query)
      