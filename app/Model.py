import sqlite3
from datetime import datetime
class Model:
    def __init__(self):
        self.connect = sqlite3.connect("todo.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""create table if not exists 
                            todo(id integer primary key autoincrement,
                            text varchar(200),
                            date Date)""")
        self.connect.commit()

    def insert(self, text):
        self.cursor.execute(f"insert into todo(text, date) values('{text}', '{datetime.utcnow}')")
        self.connect.commit()
    
    def update(self, todo_id, edit_text):
        self.cursor.execute(f"update todo set text='{edit_text}' where id={todo_id}")
        self.connect.commit()
    
    def delete(self, todo_id):
        self.cursor.execute(f"delete from todo where id={todo_id}")
        self.connect.commit()

    def viewTodos(self):
        todos = self.cursor.execute("select * from todo").fetchall()
        return todos
    # close connection
    def close(self):
        self.cursor.close()
        self.connect.close()