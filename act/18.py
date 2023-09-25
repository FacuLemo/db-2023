#Una vista con todos los empleados y su usario de Login.

#
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Empleados_usernames AS SELECT per.nombre AS empleado, usr.nombre AS username FROM empleado INNER JOIN persona AS per ON empleado.persona_id = per.id  INNER JOIN usuario AS usr ON empleado.usuario_id =usr.id"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')