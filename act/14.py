#Un script que muestro al cliente con más ventas del año.

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT YEAR(f.fecha) AS año, p.nombre AS nombre_cliente FROM factura AS f INNER JOIN cliente AS c ON f.cliente_id = c.id INNER JOIN persona AS p ON c.persona_id = p.id WHERE YEAR(f.fecha) = YEAR(CURRENT_DATE) AND anulado=0 GROUP BY p.nombre ORDER BY COUNT(*) DESC LIMIT 1"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print(result)