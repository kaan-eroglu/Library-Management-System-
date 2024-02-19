import sqlite3 as sql

def create_table():
    conn = sql.connect("user.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY,
        name text,
        lastname text,
        username text,
        password text                 
    )""")
    conn.commit()
    conn.close()

def insert(name,lastname,username, password):
    conn = sql.connect("user.db")
    cursor = conn.cursor()

    add_command = """INSERT INTO USERS(name, lastname, username, password) VALUES {}"""
    data = (name, lastname, username, password)

    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect("user.db")
    cursor = conn.cursor()

    cursor.execute ("""SELECT * from USERS""")
    list_all = cursor.fetchall()

    conn.close()
    return(list_all)

def search_username(username):
    conn = sql.connect("user.db")
    cursor = conn.cursor()

    search_command = """SELECT * from USERS WHERE username = '{}' """
    cursor.execute(search_command.format(username))

    user = cursor.fetchone()

    conn.close()
    return(user)



