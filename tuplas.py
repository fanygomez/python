#tuplas -> listas inmutablas ( no se pueden modificar)
#Se pueden omitir los parentisis
myTupla = ("Fany",1994,1,18);
mylist1 = ["Maria -4","Fany -3","Alejandro -2", "Sebas -1",15];
print(myTupla[1])

myList = list(myTupla) #convertir tupla a lista
print(myList)
#lista a tupla
newTupla = tuple(mylist1)
print(newTupla)
print(newTupla.count(15)) # Contar cuanto elementos existen (se pasa como parametro) en la tupla

print(len(newTupla)) #cuantos elementos tiene la tupla
#Tupla uniraria
tupla2 =("Fany",)
print(len(tupla2))
#Desempaquetado de tupla
#asignar cada uno de las valores de la tupla a variables
tupla3 = ("Fany",1,18,1994)
nombre, dia, mes, agnio = tupla3;