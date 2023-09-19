#script que permita agregar una nueva Localidad, de una nueva provincia de un pais que no Esta cargado en la tabla  paises.
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

nombre_pais='Uruguay'
nombre_provincia='Montevideo'
nombre_localidad='Montevideo'

sql_pais = "INSERT INTO pais (nombre) VALUES (%s)"
values=(nombre_pais,)
mycursor.execute(sql_pais,values)
nuevo_pais_id=mycursor.lastrowid

sql_prov = "INSERT INTO provincia (nombre,pais_id) VALUES (%s,%s)"
values=(nombre_provincia,nuevo_pais_id)
mycursor.execute(sql_prov,values)
nuevo_prov_id=mycursor.lastrowid

sql_localidad = "INSERT INTO localidad (nombre,provincia_id) VALUES (%s,%s)"
values=(nombre_localidad,nuevo_prov_id)
mycursor.execute(sql_localidad,values)

mydb.commit()

print(mycursor.rowcount, "registros insertados")