import sqlite3
from datetime import datetime
class Model:
    def __init__(self):
        self.connect = sqlite3.connect("todo.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""create table if not exists 
                            todo(
                            id integer primary key autoincrement,
                            user_id integer not null,
                            text varchar(200),
                            date Date,
                            foreign key(user_id) references user(id))""")
        self.cursor.execute("""create table if not exists
                            user(id integer primary key autoincrement,
                            username varchar(20), 
                            email varchar(100),
                            password varchar(200),
                            created_time Date
                            )""")
        self.connect.commit()

    def insert(self, text, user_id):
        self.cursor.execute(f"insert into todo(user_id, text, date) values({user_id},'{text}', '{str(datetime.utcnow())}')")
        self.connect.commit()
    
    def update(self, todo_id, edit_text):
        self.cursor.execute(f"update todo set text='{edit_text}' where id={todo_id}")
        self.connect.commit()
    
    def delete(self, todo_id):
        self.cursor.execute(f"delete from todo where id={todo_id}")
        self.connect.commit()

    def viewTodos(self):
        todos = self.cursor.execute("""select todo.*, user.username
                                     from todo, user 
                                    where user.id = todo.user_id""").fetchall()
        return todos
    
    def createUser(self, username, email, password):
        self.cursor.execute(f"""insert into user
                            (username, email, password, created_time)
                            values
                            ('{username}',
                              '{email}',
                                '{password}',
                                '{str(datetime.utcnow())}')""")
        self.connect.commit()
        return self.cursor.execute(f"""select * from user 
                                   where email='{email}' 
                                   and 
                                   password='{password}'""").fetchone()
    
    def deleteUser(self, user_id):
        self.cursor.execute(f"delete from user where id={user_id}")
        self.connect.commit()
    
    def user(self, email, password):
        return self.cursor.execute(f"""select 
                            * from user
                            where email='{email}'
                            and password='{password}'
                            """).fetchone()
    # close connection
    def close(self):
        self.cursor.close()
        self.connect.close()