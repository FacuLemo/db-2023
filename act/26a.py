import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Facturas_validas_mes AS SELECT factura_detalle.*,factura.anulado, factura.fecha FROM factura_detalle INNER JOIN factura ON factura_detalle.factura_id = factura.id WHERE MONTH(factura.fecha) = MONTH(CURRENT_DATE) AND factura.anulado=0"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')