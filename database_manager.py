import sqlite3 as sql

def listShark():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute('SELECT * FROM species').fetchall()
    con.close()
    return data

def insertContact(email, name):
    """
    Insert a new contact into the contact_list table.
     
    Args: email (str): Contact's email address
    name(str): Contact's name

    Returns: 
        None

    Raises: sqlite3.IntergrityError: If email already exists (UNIQUE constraint)
    """

    con = sql.connect("database/data_source.db") #Opens a connection to SQlite database file
    cur = con.cursor() #Create cursor object (OOP), act as pointer inside the database

    cur.execute("INSERT INTO contact_list (email, name) VALUES (?, ?)", (email,name))
    #Tell database to add a new row to contact_list table, (?, ?) to prevent SQL injection 

    con.commit()
    con.close() #Close databasew connection, otherwise changes will roll back

def deleteContact(email):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute("DELETE FROM contact_list WHERE email = ?", (email,))
    con.commit()
    con.close()