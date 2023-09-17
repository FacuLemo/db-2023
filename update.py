import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

sql="UPDATE producto SET nombre = %s WHERE nombre = %s"
values=("prepizza mediana", "prepizza")

mycursor.execute(sql,values)

mydb.commit()

print(mycursor.rowcount, "registros actualizado")