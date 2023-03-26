import sqlite3

def connect():
    global conn, c
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()

def create_table():
    connect()
    c.execute("""CREATE TABLE IF NOT EXISTS contacts (
    storenum text, 
    address text,
    number text
    ) """)
    conn.commit()
    conn.close()

def add_one(storenum, address, number):
    connect()
    c.execute(f"SELECT * FROM contacts WHERE storenum = '{storenum}' AND address = '{address}' AND number = '{number}'")
    result = c.fetchall()
    if len(result) == 0 and storenum != "" and address != "" and number != "":
        c.execute("INSERT INTO contacts VALUES (?, ?, ?)", (storenum, address, number))
    conn.commit()
    conn.close()
    

def show():
    connect()
    c.execute("SELECT rowid, * FROM contacts")
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def delete(id):
    connect()
    c.execute(f"DELETE FROM contacts WHERE rowid = {id}")
    conn.commit()
    conn.close()

def update(id, storenum="", address="", number=""):
    connect()
    if storenum != "":
        c.execute(f"UPDATE contacts SET storenum='{storenum}' WHERE rowid = {id}")
    if address != "":
        c.execute(f"UPDATE contacts SET address='{address}' WHERE rowid = {id}")
    if number != "":
        c.execute(f"UPDATE contacts SET number='{number}' WHERE rowid = {id}")
    conn.commit
    conn.close

create_table()