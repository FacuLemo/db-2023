#Una vista que muestre la mayor venta del mes.
"""
SELECT MONTHNAME(factura.fecha) AS mes, MAX(factura.total) AS venta_minima,

emp.nombre AS empleado_vendedor , cl.nombre AS cliente  FROM factura

INNER JOIN cliente        ON factura.cliente_id = cliente.id 

INNER JOIN empleado       ON factura.empleado_id = empleado.id

INNER JOIN persona AS emp ON empleado.persona_id = emp.id

INNER JOIN persona AS cl  ON cliente.persona_id = cl.id

WHERE anulado = 0

GROUP BY MONTH(factura.fecha)"""