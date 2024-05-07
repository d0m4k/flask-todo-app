from mysql import connector
from datetime import datetime
class Model:
    def __init__(self):
        self.connect = connector.connect(
            host="localhost",
            user="domak",
            password="audrey",
            database="test"
        )
        self.cursor = self.connect.cursor()
        self.cursor.execute("""create table if not exists
                            user(id integer primary key auto_increment,
                            username varchar(20), 
                            email varchar(100),
                            password varchar(200),
                            created_time Date
                            )""")
        self.cursor.execute("""create table if not exists 
                            todo(
                            id integer primary key auto_increment,
                            user_id integer not null,
                            text varchar(200),
                            date Date,
                            foreign key(user_id) references user(id))""")
        self.connect.commit()

    def insert(self, text, user_id): # it's
        query = "insert into todo(user_id, text, date) values(%s, %s, %s)"
        value = (user_id, text, str(datetime.utcnow()))
        self.cursor.execute(query, value)
        self.connect.commit()
    
    def update(self, todo_id, edit_text):
        self.cursor.execute(f"update todo set text='{edit_text}' where id={todo_id}")
        self.connect.commit()
    
    def delete(self, todo_id):
        self.cursor.execute(f"delete from todo where id={todo_id}")
        self.connect.commit()

    def viewTodos(self):
        self.cursor.execute("""select todo.*, user.username
                                     from todo, user 
                                    where user.id = todo.user_id""")
        todos = self.cursor.fetchall()
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
        self.cursor.execute(f"""select * from user 
                                   where email='{email}' 
                                   and 
                                   password='{password}'""")
        return self.cursor.fetchone()
    
    def deleteUser(self, user_id):
        self.cursor.execute(f"delete from user where id={user_id}")
        self.connect.commit()
    
    def user(self, email, password):
        self.cursor.execute(f"""select 
                            * from user
                            where email='{email}'
                            and password='{password}'
                            """)
        return self.cursor.fetchone()
    # close connection
    def close(self):
        self.cursor.close()
        self.connect.close()