import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sqlFactura= "SELECT MAX(id) FROM factura;"
mycursor = mydb.cursor()
mycursor.execute(sqlFactura)

id_factura= mycursor.fetchall()

sqlProductos="SELECT id,precio FROM producto WHERE id=4"
mycursor.execute(sqlProductos)

prods=mycursor.fetchall()

values=list(prods[0])
values.insert(0,id_factura[0][0])
values.insert(2,3) #cantidad de producto vendido
values=tuple(values)

print(values)

sqlFactDetalle="INSERT INTO factura_detalle (factura_id,producto_id,cantidad,precio_venta) VALUES (%s,%s,%s,%s)"
mycursor.execute(sqlFactDetalle,values)

mydb.commit()

print(mycursor.rowcount, "registro insertado")
print("ID: ",mycursor.lastrowid)


