import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

producto='Jamón crudo'
precio_venta='450'
precio_compra='330'

sql_categ = "INSERT INTO categoria_producto (nombre) VALUES (%s)"
values=("Embutidos",)
mycursor.execute(sql_categ,values)
nueva_categ=mycursor.lastrowid

sql_producto = "INSERT INTO producto (nombre,proveedor_id,precio,categoria_id,precio_compra) VALUES (%s,%s,%s,%s,%s)"
values=(producto,1 ,precio_venta,nueva_categ,precio_compra)
mycursor.execute(sql_producto,values)

mydb.commit()

print(mycursor.rowcount, "registro insertado")
print("ID: ",mycursor.lastrowid)