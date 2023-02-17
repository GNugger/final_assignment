import pyodbc


db_server = "GNPC"
db_name = "dbtest"
db_driver = "ODBC Driver 17 for SQL Server"

connection_string = f"""
DRIVER={db_driver};
SERVER={db_server};
DATABASE={db_name};
trusted_connection=yes;
"""


class DB:
    def call_db(self, query, *args):
        data = None
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        if "SELECT" in query:
            res = cur.execute(query, args)
            data = res.fetchall()
            cur.commit()
            cur.close()
        else:
            conn.execute(query, args)
        conn.commit()
        conn.close()
        return data
   

    def init_db(self):
        
        init_create_database = """
        CREATE DATABASE "dbtest";
        """
        
        
        init_employee_query = """
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY IDENTITY(1,1) NOT NULL,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            team_id INTEGER,
            leader_id INTEGER,
            title VARCHAR(20) NOT NULL,
            description VARCHAR(20) NOT NULL
            );
        """
        init_teams_query = """
        CREATE TABLE teams(
            team_id INTEGER PRIMARY KEY IDENTITY(1,1) NOT NULL,
            leader_id INTEGER,
            team_name VARCHAR(20) NOT NULL,
            FOREIGN KEY(leader_id) REFERENCES employees(id) ON DELETE SET NULL
        );
        """
        init_alter_employees = """
        ALTER TABLE employees
            ADD FOREIGN KEY(team_id)
            REFERENCES teams(team_id)
            ON DELETE SET NULL; 

        ALTER TABLE employees
            ADD FOREIGN KEY(leader_id)
            REFERENCES employees(id)
        """
        
        insert_employee_query = """
        INSERT INTO employees (first_name, last_name,team_id,leader_id,title, description)
        VALUES ('GN','Drive',1,1,'CEO','Owner');
        """
        insert_teams_query = """
        INSERT INTO teams (team_name, leader_id)
        VALUES ('Celestial Being',1);
        """
        
        
        conn = pyodbc.connect(connection_string)
        #conn.execute(init_create_database)
        conn.execute(init_employee_query)
        conn.execute(insert_employee_query)
        conn.execute(init_teams_query)
        conn.execute(insert_teams_query)
        conn.execute(init_alter_employees)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    db = DB()

    db.init_db() 