import mysql.connector

mydb = mysql.connector.connect(
    host="143.198.156.171",
    user="BD2021",
    password="BD2021itec",
    database="db_lemo",
)

mycursor = mydb.cursor()

sql_sentence = "INSERT INTO producto (nombre,proveedor_id,precio) VALUES (%s,%s,%s)"
values=("yerba Molto 500g",1,600)

mycursor.execute(sql_sentence,values)
#si los values fuesen una lista de tuplas se hace .executemany()

mydb.commit()

print(mycursor.rowcount, "registro insertado")
print("ID: ",mycursor.lastrowid)