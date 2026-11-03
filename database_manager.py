import sqlite3 as sql

def listShark():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute('SELECT * FROM species').fetchall()
    con.close()
    return data