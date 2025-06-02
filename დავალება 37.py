import sqlite3

def add_user(username,phonenumber,address):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, phonenumber, address) VALUES (?,?,?)",(username,phonenumber,address))
    conn.commit()
    conn.close()
    
def delete_user(id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DELETE FROM users where id = ?",(id,))
    conn.commit()
    conn.close()

def update_user(id,username,address):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE users set username = ?, address = ? where id = ?",(username,address,id))
    conn.commit()
    conn.close()