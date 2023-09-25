#Una vista que muestre la cantidad de productos que se contabilizan por unidad y 
#los que se contabilizan por Peso No interesan los que se contabilizan por Volumen.

#SELECT p.nombre AS producto, tv.nombre  AS tipo_de_venta FROM producto p INNER JOIN tipo_venta tv ON p.tipo_venta_id = tv.id WHERE NOT tv.nombre = 'Volumen'
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Productos_unidad_peso AS SELECT p.nombre AS producto, tv.nombre  AS tipo_de_venta FROM producto p INNER JOIN tipo_venta tv ON p.tipo_venta_id = tv.id WHERE NOT tv.nombre = 'Volumen'"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')