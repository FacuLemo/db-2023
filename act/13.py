#Una vista que muestre la menor venta del mes.

#SELECT MONTHNAME(fecha) AS mes, MAX(total) AS venta_maxima FROM factura WHERE anulado = 0 GROUP BY MONTH(fecha)
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW venta_minima_mensual AS SELECT MONTHNAME(fecha) AS mes, MIN(total) AS venta_minima FROM factura WHERE anulado = 0 GROUP BY MONTH(fecha)"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')