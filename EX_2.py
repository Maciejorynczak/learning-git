import sqlite3
from sqlite3 import Error

def create_tables():
    """ create projects and tasks tables """
    try:
        conn = sqlite3.connect(r"database.db")
        sql_create_projects_table = """
        CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY,
            nazwa text NOT NULL,
            start_date text,
            end_date text
        );
        """
        sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            project_id integer NOT NULL,
            nazwa text NOT NULL,
            opis text,
            status text NOT NULL,
            start_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );
        """
        conn.execute(sql_create_projects_table)
        conn.execute(sql_create_tasks_table)
        print("Tables created successfully.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_tables()
