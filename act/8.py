#Una Vista que muestre los resúmenes de venta mensualmente. (solo facturas que no fueron anuladas)
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW resumen_venta_mes AS SELECT MONTHNAME(fecha) AS mes, SUM(total) AS total_ventas FROM factura WHERE anulado = 0 GROUP BY MONTH(fecha)"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')