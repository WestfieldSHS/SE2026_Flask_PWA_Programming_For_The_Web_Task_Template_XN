import sqlite3 as sql

def listShark():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM species ORDER BY common_name COLLATE NOCASE ASC')
    data = cur.fetchall()
    con.close()
    return data

def listSpeciesByConservationStatus(conservation_status):
  con = sql.connect("database/data_source.db")
  cur = con.cursor()

  cur.execute(
      "SELECT * FROM species WHERE conservation_status = ? ORDER BY common_name COLLATE NOCASE ASC",
      (conservation_status,),)
  data =cur.fetchall()
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
    try:
        con = sql.connect("database/data_source.db") #Opens a connection to SQlite database file
        cur = con.cursor() #Create cursor object (OOP), act as pointer inside the database

        cur.execute("INSERT INTO contact_list (email, name) VALUES (?, ?)", (email,name))
        #Tell database to add a new row to contact_list table, (?, ?) to prevent SQL injection 
        con.commit()
    except Exception:
        con.rollback()
        raise #re-raise IntegrityError so main.py can catch it

    finally:
        con.close() #Close databasew connection, otherwise changes will roll back
    return (True, "Contact added successfully")
    

def deleteContact(email):
    con = sql.connect("database/data_source.db")

    cur = con.cursor()
    cur.execute("DELETE FROM contact_list WHERE email = ?", (email,))
    con.commit()


    con.close() #close, even when there's an error happens

def listSharkbystatus(conservation_status):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        data = cur.execute("SELECT * FROM species WHERE conservation_status = ?", (conservation_status,)).fetchall()
    return data