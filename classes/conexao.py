import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aula"
        )
    return mydb