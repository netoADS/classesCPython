import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="3.89.143.162",
        user="root",
        password="senai1999",
        database="livros"
        )
    return mydb