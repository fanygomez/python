import sqlite3

miConexion = sqlite3.connect("test")
miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTS(NAME VARCHAR(50), PRICE INTEGER, SECTION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTS VALUES('BALON',80,'DEPORTES')")
ListProductos = [
    ("Camiseta",10,"Deportes"),
    ("Jarrón",90,"Cerámica"),
    ("Camión",20,"Juguetería")
]
#miCursor.executemany("INSERT INTO PRODUCTS VALUES(?,?,?)",ListProductos)
#miConexion.commit()
miCursor.execute("SELECT * FROM PRODUCTS")
data = miCursor.fetchall()
print(data)

for producto in data:
    print("Nombre articulo: ", producto[0], " Seccion: ", producto[2])
miConexion.close()