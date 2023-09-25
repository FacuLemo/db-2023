#Una consulta de Union que muestre un listado de los proveedores y clientes 
#del sistema en una misma columna, mostrar direccion y su sexo. (Listado de saludos fin de año).

#SELECT p.nombre, l.nombre AS localidad, ts.nombre FROM proveedor pr INNER JOIN persona p ON pr.persona_id = p.id INNER JOIN tipo_sexo ts ON p.sexo_id = ts.id INNER JOIN localidad l ON p.localidad_id = l.id
#UNION  
#SELECT p.nombre, l.nombre, ts.nombre FROM cliente cl INNER JOIN persona p ON cl.persona_id = p.id  INNER JOIN tipo_sexo ts ON p.sexo_id = ts.id INNER JOIN localidad l ON p.localidad_id = l.id

import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "SELECT p.nombre, l.nombre AS localidad, ts.nombre FROM proveedor pr INNER JOIN persona p ON pr.persona_id = p.id INNER JOIN tipo_sexo ts ON p.sexo_id = ts.id INNER JOIN localidad l ON p.localidad_id = l.id UNION SELECT p.nombre, l.nombre, ts.nombre FROM cliente cl INNER JOIN persona p ON cl.persona_id = p.id  INNER JOIN tipo_sexo ts ON p.sexo_id = ts.id INNER JOIN localidad l ON p.localidad_id = l.id"
mycursor = mydb.cursor()
mycursor.execute(sql)


result = mycursor.fetchall()
print('Resultado de consulta:')
print(result)