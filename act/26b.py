import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Productos_no_vendidos_mes AS SELECT p.id, p.nombre FROM producto p LEFT OUTER JOIN Factdetalle_validas_mes fvm ON fvm.producto_id =  p.id WHERE fvm.producto_id IS NULL"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')