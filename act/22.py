#Una vista que de el resultado de ganancia mensual de cada producto teniendo en cuenta el costo de compra del mismo.

#
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Ganancias_producto_mensuales AS SELECT p.nombre,(SUM(cantidad) * p.precio)-(SUM(cantidad) * p.precio_compra) AS ganancia FROM factura_detalle fd INNER JOIN producto AS p ON fd.producto_id = p.id INNER JOIN factura AS f ON fd.factura_id =f.id WHERE f.anulado=0 AND MONTH(f.fecha) = MONTH(CURRENT_DATE) GROUP BY producto_id"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')