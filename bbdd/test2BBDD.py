import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()
# miCursor.execute('''
#     CREATE TABLE PRODUCTS(
#     CODE VARCHAR(4) PRIMARY KEY,
#     NAME VARCHAR(50),
#     PRICE INTEGER,
#     SECTION VARCHAR(20))''')

# miCursor.execute('''
#     CREATE TABLE PRODUCTS(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NAME VARCHAR(50) UNIQUE,
#     PRICE INTEGER,
#     SECTION VARCHAR(20))''')
# productos = [
#     ("PELOTA",20,"JUGUETERIA"),
#     ("PANTALON",90,"CONFECCION"),
#     ("Camión",20,"Juguetería")
# ]
# miCursor.executemany("INSERT INTO PRODUCTS VALUES(NULL,?,?,?)",productos)
# miCursor.executemany("INSERT INTO PRODUCTS VALUES('AR03','TREN',15,'JUGUETERIA')")
miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTS WHERE SECTION='CONFECCION'")
data = miCursor.fetchall()
print(data)
#UPDATE
miCursor.execute("UPDATE PRODUCTS SET PRICE=35 WHERE NAME='PELOTA'")
data = miCursor.fetchall()
print(data)
miCursor.execute("SELECT * FROM PRODUCTS")
data = miCursor.fetchall()
print(data)
#DELETE
miCursor.execute("DELETE FROM PRODUCTS WHERE ID=3")
data = miCursor.fetchall()
print(data)
miConexion.close()