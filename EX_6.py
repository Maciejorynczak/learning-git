import sqlite3
from sqlite3 import Error

def delete_task(task_id):
    """ delete a task by task id """
    try:
        conn = sqlite3.connect(r"database.db")
        sql = 'DELETE FROM tasks WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (task_id,))
        conn.commit()
        print("Task deleted.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    delete_task(1)
