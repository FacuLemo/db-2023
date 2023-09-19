#Un script con el resultado de lo vendido por cada artículo de las facturas que no estén anuladas.
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT  producto.id, producto.nombre,SUM(factura_detalle.cantidad) FROM factura_detalle INNER JOIN producto ON factura_detalle.producto_id=producto.id INNER JOIN factura ON factura_detalle.factura_id = factura.id  WHERE factura.anulado=0 GROUP BY producto.nombre" 


mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print(result)