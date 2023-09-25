#Un script que muestre las ventas por provincia (cantidad y suma).
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT SUM(factura.total) AS total_venta, COUNT(factura.total) AS cantidad, prov.nombre AS provincia FROM factura INNER JOIN empleado as emp ON factura.empleado_id  = emp.id INNER JOIN sucursal as suc ON emp.sucursal_id = suc.id INNER JOIN localidad as loc ON suc.localidad_id = loc.id INNER JOIN provincia as prov ON loc.provincia_id = prov.id  WHERE anulado = 0 GROUP BY prov.nombre "
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print(result)