#Una vista con todos los clientes y si tienen usuario para ingresar web o solamente han comprado en modo presencial (o sea no tienen usuario).

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Clientes_usernames AS SELECT per.nombre AS cliente, usr.nombre AS username FROM cliente INNER JOIN persona AS per ON cliente.persona_id = per.id LEFT JOIN usuario AS usr ON cliente.cuenta_usuario_id =usr.id"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')