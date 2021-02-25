# Diccinarios -> nos permiten almacenar valores de dirente tipo e incluso listas
# Ej clave: valor
#No pueden existir dos claves iguales
#No estan ordenados
#El orden es indiferente a la hora de almancenar la informacion
#Eje, capitales
diccionario = {"Alemania":"Berlin","Farcia":"Paris"}
print(diccionario)
#Agregar elemento
diccionario["El Salvador"] = "San Salvador"
print(diccionario)
#Eliminar
del diccionario["Farcia"]
print(diccionario)

diccionario2 = {"Alemania":"Berlin","Farcia":"Paris",23:"Jordan","Mosqueteros":3}
print(diccionario2)
#tupla -> diccionari
mitupla = ["Guatemala","Honduras","El Salvador"]
diccionario3 = {mitupla[0]:"GT",mitupla[1]:"HN" }
print(diccionario3)

diccionario4 = {23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
#devolver las claves
print(diccionario4.keys())
#devolver los valores
print(diccionario4.values())
print(diccionario4)

#devolver los valores
print(len(diccionario4))
print(diccionario4)
print("VERIFICAR ACCESO")

edad_usuario = int(input("Introducir tu edad, por favor"))

if edad_usuario < 18:
    print("No puedes pasar")
else:
    print("Pasa!")
