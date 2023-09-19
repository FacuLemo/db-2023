#Una Vista que muestre todos los clientes Activos
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW clientes_activos AS SELECT id, persona_id, usuario_id, limite_cuenta_corriente, observaciones FROM cliente WHERE activo=1"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)