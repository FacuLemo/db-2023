#ver id máximo (ultimo) de la table factura
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT MAX(id), fecha, anulado FROM factura;"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print(result)