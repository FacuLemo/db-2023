#Un script que indique que empleado es el que mas ventas realizo en los ultimos 3 meses, 
#agregando el sexo y la sucursal en la que atiende y de que Localidad es Oriundo.

#SELECT p.nombre, COUNT(*) AS ventas , ts.nombre AS sexo, s.nombre AS sucursal, l.nombre AS localidad FROM empleado e INNER JOIN persona p ON e.persona_id = p.id INNER JOIN localidad l ON p.localidad_id = l.id INNER JOIN tipo_sexo ts ON p.sexo_id = ts.id INNER JOIN sucursal s ON e.sucursal_id = s.id INNER JOIN factura f ON f.empleado_id = e.id WHERE  f.anulado=0 AND f.fecha >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) GROUP BY p.nombre ORDER BY ventas DESC LIMIT 1

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT p.nombre, COUNT(*) AS ventas , ts.nombre AS sexo, s.nombre AS sucursal, l.nombre AS localidad FROM empleado e INNER JOIN persona p ON e.persona_id = p.id INNER JOIN localidad l ON p.localidad_id = l.id INNER JOIN tipo_sexo ts ON p.sexo_id = ts.id INNER JOIN sucursal s ON e.sucursal_id = s.id INNER JOIN factura f ON f.empleado_id = e.id WHERE  f.anulado=0 AND f.fecha >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) GROUP BY p.nombre ORDER BY ventas DESC LIMIT 1"
mycursor = mydb.cursor()
mycursor.execute(sql)


result = mycursor.fetchall()
print('Resultado de consulta:')
print(result)
