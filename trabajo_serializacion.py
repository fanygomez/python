import pickle

list_nombres = ["Alejandro","Leo","Dilan","Sabita"];

fichero_binario = open("lista_nombres","wb") #wb: write binary

pickle.dump(list_nombres,fichero_binario)

fichero_binario.close()
#Borrar de la memoria
del(fichero_binario)

fichero = open("lista_nombres","rb") #read binary
lista = pickle.load(fichero)
print(lista)