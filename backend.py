import sqlite3

def connect():
    """
    It creates a database called employee.db and creates a table for employeedetails.
    """
    conn=sqlite3.connect("employee.db")
    cur=conn.cursor()  
    cur.execute("CREATE TABLE IF NOT EXISTS employeedetails (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,department TEXT,identity INTEGER,salary INTEGER)")
    conn.commit()
    conn.close()

def view():
    """
    It connects to the database, fetches all the items in db, closes the connection, and
    returns the results.
    """
    conn=sqlite3.connect("employee.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employeedetails")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",department="",identity="",Salary=""):
    """
    It requires atleast one parameter to be passed in. It connects to the database, fetches all the items in db with particular search criteria, closes the connection, and returns the results.
    """
    conn=sqlite3.connect("employee.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employeedetails WHERE name=? OR department=? OR identity=? OR salary=?",(name,department,identity,Salary))
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(name,department,identity,Salary):
    """
    It takes in 4 parameters (name, department, identity, price) and inserts them into the database
    """
    conn=sqlite3.connect("employee.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO employeedetails VALUES(NULL,?,?,?,?)",(name,department,identity,Salary))
    conn.commit()
    conn.close()

    
def delete(id):
    """
    It takes the details of the employee as an argument and deletes the book from the database
    """
    conn=sqlite3.connect("employee.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM employeedetails WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, name, department, identity, Salary):
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute("UPDATE employeedetails SET name=?, department=?, identity=?, salary=? WHERE id=?", (name, department, identity, Salary, id))
    conn.commit()
    conn.close()

connect()