import sqlite3
from sqlite3 import Error

def add_project(project):
    """ add a new project to the projects table """
    try:
        conn = sqlite3.connect(r"database.db")
        sql = '''INSERT INTO projects(nazwa, start_date, end_date)
                 VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        print("Project added successfully.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_task(task):
    """ add a new task to the tasks table """
    try:
        conn = sqlite3.connect(r"database.db")
        sql = '''INSERT INTO tasks(project_id, nazwa, opis, status, start_date, end_date)
                 VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        print("Task added successfully.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    project = ("Zrób zadania", "2024-08-18", "2024-08-20")
    add_project(project)

    task_1 = (1, "Zadanie 1", "Opis zadania 1", "started", "2024-08-18 08:00:00", "2024-08-18 12:00:00")
    add_task(task_1)
