from io import open
#Fase #1 Crear y abri
archivo_texto = open("archivo.texto","w")

#Fase #2 Manipulacion
frase ="Estudando Python \n desde hace 3 dias."
archivo_texto.write(frase)

#Fase #3 Cerrar
archivo_texto.close()

#Abrir en modo lectura
archivo_texto2 = open("archivo.texto","r")
texto = archivo_texto2.read()
archivo_texto2.close()
print(texto)
#Abrir en modo readlines, busqueda linea a linea
archivo_texto3 = open("archivo.texto","r")
lineas_texto = archivo_texto3.readlines()
archivo_texto3.close()
print(lineas_texto[0])

#Abri archivo para agregar informacion

archivo_agregar = open("archivo.texto","a")#a = append

archivo_agregar.write("Ruta de aprendizaje -> Crear APIs")

archivo_agregar.close()