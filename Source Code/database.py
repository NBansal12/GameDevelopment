import sqlite3

def createTable();:
    connection= sqlite3.connect("gamerdetails.db")
    
    connection.execute("CREATE TABLE GAMERDETAILS (USERNAME TEXT NOT NULL, GENDER))
    connection.execute("INSERT INTO GAMERDETAILS VALUES())
    
