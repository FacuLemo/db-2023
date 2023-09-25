#Un script que sirva para la insercion de un nuevo empleado (tener en cuenta que se necesita que se le genere usuario)
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

nombre_empleado='Tadeo Pariani'
nombre_login='tadeoquent'
pass_login='tadeo123'
sucursal_id=1 #rio cuarto

sql_pers = "INSERT INTO persona (nombre,email,localidad_id,sexo_id,tipo_documento_id,documento,telefono_id,estado_fiscal_id,numero_telefono,usuario_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values=(nombre_empleado,'quentin@gmail.com',2687,1,1,'44999111',1,3,'154300300',1)
mycursor.execute(sql_pers,values)
nueva_pers_id=mycursor.lastrowid

sql_cuenta = "INSERT INTO usuario (nombre,password,persona_id,tipo_usuario_id) VALUES (%s,%s,%s,%s)"
values=(nombre_login,pass_login,nueva_pers_id,4) #4 es el tipo usr empleado
mycursor.execute(sql_cuenta,values)
nueva_cuenta_id=mycursor.lastrowid

sql_emp = "INSERT INTO empleado (persona_id,sucursal_id,cargo_id,usuario_id) VALUES (%s,%s,%s,%s)"
values=(nueva_pers_id,sucursal_id,2,nueva_cuenta_id) #2 es vendedor
mycursor.execute(sql_emp,values)

mydb.commit()

print(mycursor.rowcount, "registros insertados")