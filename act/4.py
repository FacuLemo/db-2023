#conseguir el precio real de la factura sumando las (cant*precio) de los articulos
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

factura_id = mycursor.fetchall()
factura_id = factura_id[0]


sqlFactDetalle="SELECT cantidad, precio_venta FROM factura_detalle WHERE factura_id=%s"
mycursor.execute(sqlFactDetalle,factura_id)
prods=mycursor.fetchall()


total=0
for prod in prods:
    cant,precio=prod
    precioProd=precio*cant
    total+=precioProd

mydb.commit()

print("el precio real es: ",total)