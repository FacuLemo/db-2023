#Una vista que muestre que sucursal es la que más ventas tienen
#SELECT s.nombre, SUM(f.total) FROM factura f INNER JOIN empleado e ON f.empleado_id =e.id INNER JOIN sucursal s ON e.sucursal_id =s.id WHERE f.anulado=0 GROUP BY s.nombre
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Ventas_por_sucursal AS SELECT s.nombre, SUM(f.total) AS total_acumulado FROM factura f INNER JOIN empleado e ON f.empleado_id =e.id INNER JOIN sucursal s ON e.sucursal_id =s.id WHERE f.anulado=0 GROUP BY s.nombre ORDER BY SUM(f.total) DESC"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')