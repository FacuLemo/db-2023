#Un script que diga la cantidad de clientes masculinos y femeninos que compraron en el último mes.
"""
SELECT ts.nombre AS sexo, COUNT(*) AS cantidad FROM factura INNER JOIN cliente AS cl ON factura.cliente_id = cl.id
 INNER JOIN persona as per ON cl.persona_id  = per.id INNER JOIN tipo_sexo as ts ON per.sexo_id = ts.id
   WHERE anulado = 0 AND MONTH(fecha)= MONTH(CURDATE()) GROUP BY ts.nombre ORDER BY cantidad DESC
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT ts.nombre AS sexo, COUNT(*) AS cantidad FROM factura INNER JOIN cliente AS cl ON factura.cliente_id = cl.id INNER JOIN persona as per ON cl.persona_id  = per.id INNER JOIN tipo_sexo as ts ON per.sexo_id = ts.id WHERE anulado = 0 AND MONTH(fecha)= MONTH(CURDATE()) GROUP BY ts.nombre ORDER BY cantidad DESC"
mycursor = mydb.cursor()
mycursor.execute(sql)


result = mycursor.fetchall()
print('Resultado de consulta:')
print(result)