#Una vista que muestre la cantidad de clientes agrupados por cada tipo de condicion fiscal.
#SELECT ef.nombre, p.nombre FROM cliente c INNER JOIN persona p ON c.persona_id = p.id INNER JOIN estado_fiscal ef ON p.estado_fiscal_id = ef.id  WHERE visible = 1 ORDER BY ef.nombre
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Clientes_condicion_fiscal AS SELECT ef.nombre AS estado_fiscal, p.nombre, p.email FROM cliente c INNER JOIN persona p ON c.persona_id = p.id INNER JOIN estado_fiscal ef ON p.estado_fiscal_id = ef.id  WHERE visible = 1 ORDER BY ef.nombre"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')