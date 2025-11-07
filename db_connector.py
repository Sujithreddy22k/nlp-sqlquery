#db_connector.py
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    server = os.environ["SERVER"]
    database = os.environ["DATABASE"]
    username = os.environ["db_user"]
    password = os.environ["PASSWORD"]

    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password}"
    )
    return pyodbc.connect(connection_string)

