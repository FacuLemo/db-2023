#Una vista que muestre la mayor venta del mes.
#SELECT MONTHNAME(fecha) AS mes, MAX(total) AS venta_maxima FROM factura WHERE anulado = 0 GROUP BY MONTH(fecha)
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW venta_maxima_mensual AS SELECT MONTHNAME(fecha) AS mes, MAX(total) AS venta_maxima FROM factura WHERE anulado = 0 GROUP BY MONTH(fecha)"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')





"""
SELECT MONTHNAME(factura.fecha) AS mes, MAX(factura.total) AS venta_maxima,

emp.nombre AS empleado_vendedor , cl.nombre AS cliente  FROM factura

INNER JOIN cliente        ON factura.cliente_id = cliente.id 

INNER JOIN empleado       ON factura.empleado_id = empleado.id

INNER JOIN persona AS emp ON empleado.persona_id = emp.id

INNER JOIN persona AS cl  ON cliente.persona_id = cl.id

WHERE anulado = 0

GROUP BY MONTH(factura.fecha)"""