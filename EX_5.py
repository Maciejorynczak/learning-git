import sqlite3
from sqlite3 import Error

def update_task_status(task_id, status):
    """ update the status of a task """
    try:
        conn = sqlite3.connect(r"database.db")
        sql = ''' UPDATE tasks
                  SET status = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (status, task_id))
        conn.commit()
        print("Task status updated.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    update_task_status(1, "completed")

