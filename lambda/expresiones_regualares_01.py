'''Son una secuencia de caracteres que forman un patron de búsqueda.
¿ Para que sirven?
PAra el trabajo y procesamiento de texton
Eje:
- Buscar un texto que se ajusta a un formato determinado ( email)
-
'''

import  re

cadena = " Vamos aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoBuscar="Python"
# print(re.search("aprenderr",cadena))
textoEncontrado = re.search(textoBuscar,cadena)
if textoEncontrado is not None:
    print("He encontrado el texto")
    print(textoEncontrado.start())#inicia en el caracter
    print(textoEncontrado.end())#Termina en el caracter
    print(textoEncontrado.span())
else:
    print("No he econtrado el texto")
#findall
print("findall()")
textoEncontrado2 = re.findall(textoBuscar,cadena)
print(textoEncontrado2)