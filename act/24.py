#Un script que permita ingresar una compra completa.

import mysql.connector
mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

#act1 insert fact
sql_sentence = "INSERT INTO factura (cliente_id,numero_factura,metodo_pago_id,tipo_factura_id,empleado_id) VALUES (%s,%s,%s,%s,%s)"
values=(4,30,3,1,1)

mycursor.execute(sql_sentence,values)
id_factura= mycursor.lastrowid

#ACT3 INSERT A FACT DETALLE
sqlProductos="SELECT id,precio FROM producto WHERE id=2" #select producto (s)
mycursor.execute(sqlProductos)

prods=mycursor.fetchall()

values=list(prods[0])
values.insert(0,id_factura)
values.insert(2,3) #cantidad de producto vendido
values=tuple(values)

print(values) #(idFactura,idprod,cantprod, precioprod)

sqlFactDetalle="INSERT INTO factura_detalle (factura_id,producto_id,cantidad,precio_venta) VALUES (%s,%s,%s,%s)"
mycursor.execute(sqlFactDetalle,values)
mydb.commit()

#ACT5 ACTUALIZAR PRECIO
idfacttupla=(id_factura,)

sqlFactDetalle="SELECT cantidad, precio_venta FROM factura_detalle WHERE factura_id=%s"
mycursor.execute(sqlFactDetalle,idfacttupla)
prods=mycursor.fetchall()

total=0
for prod in prods:
    cant,precio=prod
    precioProd=precio*cant
    total+=precioProd

values=(total,id_factura)


sqlUpdate="UPDATE factura SET total = %s WHERE id = %s"
mycursor.execute(sqlUpdate,values)
mydb.commit()

print(total)
print("ID: ",mycursor.lastrowid)