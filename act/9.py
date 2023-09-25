#Una vista que muestre las localidades solo de argentina
import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

sql= "CREATE VIEW localidades_argentinas AS SELECT localidad.nombre,provincia.nombre AS provincia FROM localidad INNER JOIN provincia ON localidad.provincia_id = provincia.id  INNER JOIN pais ON provincia.pais_id = pais.id WHERE pais.nombre = 'Argentina' ORDER BY provincia.nombre"
mycursor = mydb.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()

print('vista creada.')