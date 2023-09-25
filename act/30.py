#Una vista que muestro una leyenda para los vendedores que merecen cobrar Bono fin de año.
# (Condición para esto: que tengan ventas por más de $10000 (bono de $2000) ,
# en el caso de que el empleado no sea vendedor será un Bono fijo de $1000) en el listado deben salir  
#los empleados que cobran bono anual aclarando cada situación

#SELECT p.nombre AS empleado, ce.nombre AS cargo, IF(ce.nombre='Vendedor' AND SUM(f.total)>10000 ,'$2000','$1000') AS bono_correspondiente FROM empleado e INNER JOIN factura AS f ON f.empleado_id = e.id  INNER JOIN cargo_empleado AS ce  ON e.cargo_id = ce.id INNER JOIN persona p ON e.persona_id = p.id WHERE ANULADO = 0 GROUP BY p.nombre

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW Empleados_bono AS SELECT p.nombre AS empleado, ce.nombre AS cargo, IF(ce.nombre='Vendedor' AND SUM(f.total)>10000 ,'$2000','$1000') AS bono_correspondiente FROM empleado e INNER JOIN factura AS f ON f.empleado_id = e.id  INNER JOIN cargo_empleado AS ce  ON e.cargo_id = ce.id INNER JOIN persona p ON e.persona_id = p.id WHERE ANULADO = 0 GROUP BY p.nombre"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')