import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT id, nombre, proveedor_id, precio FROM producto"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)