#Una Vista que de los artículos más vendidos y que genere un nuevo campo con la leyenda "Producto Top"
#cuando la  cantidades vendidas superen a 50 por mes. En caso de ser menor la leyenda debe ser "Producto Estándar"

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Produtos_top_standar_mes AS SELECT p.nombre, IF(COUNT(*)>=50, 'producto top','producto standar') as producto_ventas_tipo, COUNT(*) AS cantidad FROM factura_detalle fd INNER JOIN producto p ON fd.producto_id = p.id INNER JOIN factura f ON fd.factura_id = f.id WHERE f.anulado=0 AND MONTH(fecha)= MONTH(CURDATE()) GROUP BY p.nombre"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')