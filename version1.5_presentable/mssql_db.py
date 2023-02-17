import pyodbc
import os

db_server = "GNPC"
db_name = "dbtest_new"
db_driver = "ODBC Driver 17 for SQL Server"

connection_string = f"""
DRIVER={db_driver};
SERVER={db_server};
DATABASE={db_name};
trusted_connection=yes;
"""
# Not fully fleshed out since i got some weird issues that i havn't been able to put time to solve but it was working on my version 1.0 of the code which is very barebones 

class DB:
    
    db_name: str
    def __init__(self, db_name: str):
        self.db_name = db_name
        if not os.path.exists(self.db_name):
            self.__set_up_db()
    
    def __set_up_db(self):
        conn = pyodbc.connect(self.db_name)
        with open("gn_setup.sql","r") as file:
            script = file.read()
            conn.excutescript(script)
            conn.commit
        conn.close()
    
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