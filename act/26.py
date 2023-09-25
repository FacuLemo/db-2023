#Una vista que muestre qué artículos no son vendidos en el mes.
import mysql.connector

########################
#PROCEDIMIENTO
#PARA LAS VISTAS VER 26a Y 26b
#############

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "DROP TEMPORARY TABLE if EXISTS temp_comp; CREATE TEMPORARY TABLE IF NOT EXISTS temp_comp AS (SELECT factura_detalle.*,factura.anulado, factura.fecha FROM factura_detalle  INNER JOIN factura ON factura_detalle.factura_id = factura.id WHERE MONTH(factura.fecha) = MONTH(CURRENT_DATE) AND factura.anulado=0); SELECT p.id, p.nombre FROM producto p LEFT OUTER JOIN temp_comp temp ON temp.producto_id =  p.id WHERE temp.producto_id IS NULL "
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('procedimiento terminado.')
print(result)


#intentos fallidos:
"""
DROP TEMPORARY TABLE if EXISTS temp_comp;
CREATE TEMPORARY TABLE IF NOT EXISTS temp_comp
AS (SELECT factura_detalle.*,factura.anulado, factura.fecha FROM factura_detalle 
INNER JOIN factura ON factura_detalle.factura_id = factura.id 
WHERE MONTH(factura.fecha) = MONTH(CURRENT_DATE) AND factura.anulado=0) ;

SELECT p.id, p.nombre FROM producto p 
LEFT OUTER JOIN temp_comp temp ON temp.producto_id =  p.id
WHERE temp.producto_id IS NULL
"""

"""
SELECT p.id, p.nombre FROM 
(SELECT * FROM factura_detalle fd INNER JOIN factura AS f ON fd.factura_id =f.id 
WHERE MONTH(f.fecha) = MONTH(CURRENT_DATE) AND f.anulado=0)

RIGHT OUTER JOIN producto AS p ON fd.producto_id = p.id 
WHERE fd.producto_id IS NULL
"""

"""
SELECT p.id, p.nombre FROM factura_detalle fd 
INNER JOIN factura AS f ON fd.factura_id =f.id 
RIGHT JOIN producto p ON fd.producto_id = p.id
WHERE MONTH(f.fecha) = MONTH(CURRENT_DATE) AND f.anulado=0 AND fd.producto_id IS NULL
"""