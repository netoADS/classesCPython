import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senai1999",
        database="livros"
        )
    return mydb