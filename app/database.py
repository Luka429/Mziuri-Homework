import sqlite3

def init_db():
     conn = sqlite3.connect("info.db")
     c = conn.cursor()
     conn.row_factory = sqlite3.Row
     c.execute(
          """
            CREATE TABLE IF NOT EXISTS info (
               id integer primary key autoincrement,
               username text,
               password text
            )
          """
     )
     conn.commit()
     conn.close()

def register(username, password):
     conn = sqlite3.connect("info.db")
     c = conn.cursor()
     c.execute("insert into info (username, password) values (?, ?)", (username, password))
     conn.commit()
     conn.close()

def update(pk, username):
     conn = sqlite3.connect("info.db")
     c = conn.cursor()
     c.execute("update info set username = ? where id = ?", (username,pk))
     rows = c.fetchall()
     conn.commit()
     conn.close()
     if rows:
          return "Action was succesful"
     return "NOT FOUND"

def delete(pk):
     conn = sqlite3.connect("info.db")
     c = conn.cursor()
     c.execute("delete from info where id = ?", (pk,))
     rows = c.fetchall()
     conn.commit()
     conn.close()
     if rows:
          return "Action was succesful"
     return "NOT FOUND"

def login(username,password):
     conn = sqlite3.connect("info.db")
     c = conn.cursor()
     c.execute("SELECT * FROM info WHERE username = ? AND password = ?",(username,password))
     rows = c.fetchall()
     conn.commit()
     conn.close()
     if rows:
      return "AUTHENTICATED"
     return "NOT FOUND"

def users_get():
    conn = sqlite3.connect("info.db")
    c = conn.cursor()
    c.execute('SELECT * FROM info')
    rows = c.fetchall()
    conn.commit()
    conn.close()

    if rows:
      return rows
    return "Not found"


def user_get(pk):
    conn = sqlite3.connect("info.db")
    c = conn.cursor()
    c.execute("SELECT * from info WHERE id = ?",(pk,))
    rows = c.fetchall()
    conn.commit()
    conn.close()

    if rows:
      return rows
    return "Not found"


