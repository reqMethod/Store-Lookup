import sqlite3

def connect():
    global conn, c
    conn = sqlite3.connect("sqliteclass.db")
    c = conn.cursor()

def create_table():
    connect()
    c.execute("""CREATE TABLE IF NOT EXISTS "dw_Loc" (
    "LOC_ID" VARCHAR(10),
    "LOC_NM" VARCHAR(100),
    "LOC_TEL_NBR" VARCHAR(50),
    "LOC_EMAIL_TXT" VARCHAR(250),
    "ADDR_LN_1_TXT" VARCHAR(100),
    "TRIAL491" CHAR(1)) """)
    conn.commit()
    conn.close()
    

def add_one(storenum, name, number, email, address, trial):
    connect()
    c.execute(f"SELECT * FROM dw_Loc WHERE LOC_ID = '{storenum}' AND LOC_NM = '{name}' AND LOC_TEL_NBR = '{number}' AND LOC_EMAIL_TXT = '{email}' AND ADDR_LN_1_TXT = '{address}' AND TRIAL491 = '{trial}'")
    result = c.fetchall()
    if len(result) == 0 and storenum != "" and name != "" and number != "" and email != "" and address != "" and trial !="":
        c.execute("INSERT INTO dw_Loc VALUES (?, ?, ?, ?, ?, ?)", (storenum, name, number, email, address, trial))
    conn.commit()
    conn.close()
    
    

def show():
    connect()
    c.execute("SELECT rowid, * FROM dw_Loc")
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def showSpecific(storenum):
    connect()
    c.execute(f"SELECT rowid, * FROM dw_Loc WHERE LOC_ID ='{storenum}'")
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def delete(id):
    connect()
    c.execute(f"DELETE FROM dw_Loc WHERE rowid = {id}")
    conn.commit()
    conn.close()
    

def update(id, storenum="", name="", number="", email="", address="", trial=""):
    connect()
    if storenum != "":
        c.execute(f"UPDATE dw_Loc SET LOC_ID='{storenum}' WHERE rowid = {id}")
    if name != "":
        c.execute(f"UPDATE dw_Loc SET LOC_NM='{name}' WHERE rowid = {id}")
    if number != "":
        c.execute(f"UPDATE dw_Loc SET LOC_TEL_NBR='{number}' WHERE rowid = {id}")
    if email != "":
        c.execute(f"UPDATE dw_Loc SET LOC_EMAIL_TXT='{email}' WHERE rowid = {id}")
    if address != "":
        c.execute(f"UPDATE dw_Loc SET ADDR_LN_1_TXT='{address}' WHERE rowid = {id}")
    if trial != "":
        c.execute(f"UPDATE dw_Loc SET TRIAL491='{trial}' WHERE rowid = {id}")
    conn.commit
    conn.close
    

create_table()