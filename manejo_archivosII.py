from io import open

archivo_texto = open("archivo.texto","r+") # r+ lectura y escritura
#archivo_texto.seek(11)
#archivo_texto.seek(len(archivo_texto.read())/2)
archivo_texto.write("Inicia el texto")
#archivo_texto.seek(len(archivo_texto.readline()))

lista_texto = archivo_texto.readlines()
lista_texto[1] = "Esta linea ha sido incluida desde exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()


#Cambiar de posicion  del cursor