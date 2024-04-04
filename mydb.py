import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObject = dataBase.cursor()

createdatabase = cursorObject.execute("CREATE DATABASE myda")
print("all done")