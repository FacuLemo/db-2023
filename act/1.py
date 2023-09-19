#inserte un registro en la tabla factura

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

sql_sentence = "INSERT INTO factura (cliente_id,numero_factura,metodo_pago_id,tipo_factura_id,total,empleado_id) VALUES (%s,%s,%s,%s,%s)"
values=(4,22,3,1,'0',1)

mycursor.execute(sql_sentence,values)

mydb.commit()

print(mycursor.rowcount, "registro insertado")
print("ID: ",mycursor.lastrowid)