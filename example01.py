print("Hola mundo")
a =  0
for i in range(5):
	a+=1
	print(a)

#Crear funciones
#La identacion es importante para indicar lo que va dentro de la funcion
def menssage(test):
	print("hello world "+test)
#Ejecutar
menssage("2021")
#Listas -> arrays
mylist = ["Maria -4","Fany -3","Alejandro -2", "Sebas -1"];
mylist2 = ["swiss","Gomez"];
print(mylist[-1])
print(mylist[0:3])
#Agregar lista
mylist.append("Sandra") #agrega al final
mylist.insert(2,"Leo") # agregar a un  indice espeficio
mylist.extend(["Test",78.9,True]) # agegregar o unir otra lista
mylist.index("Sandra") #En que indice se encuentra
print("Sandra" in mylist) #Validar si existe
print(mylist[:])
mylist.remove("Leo") #eliminar un elemento
print(mylist[:])
mylist.pop() #Eliminar el ultimo elemento
#unir dos listas
mylist3 = mylist2 + mylist
print(mylist[:])
mylist4 = ["Maria -4","Fany -3","Alejandro -2", "Sebas -1"] * 3;
#repetir listas
print(mylist[:])
