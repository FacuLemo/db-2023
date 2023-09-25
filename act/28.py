#Una lista estadística del porcentaje de ventas sobre el total de ventas de acuerdo a cada sucursal.

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT nombre, total_acumulado, (total_acumulado * 100.0 / (SELECT SUM(total_acumulado) FROM Ventas_por_sucursal vps2)) AS porcentaje FROM Ventas_por_sucursal vps "
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print(result)