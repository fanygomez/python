import re
#match() : Siempre busca al principio
#search(): Busca en toda la cadena
nombre01 = "Sandra Gomex"
nombre02 = "868484527"
nombre03 = "Dilan Bonilla"
codigo = "jdfdsnkdsnfnknksd27"
if re.match("\d",nombre02,re.IGNORECASE):
    print("Hemos encontrado el  numero")
else:
    print("No lo hemos encontrado")
#Patron de busqueda para cadenas grandes
if re.search("bonilla",nombre03,re.IGNORECASE):
    print("Hemos encontrado el  nombre")
else:
    print("No lo hemos encontrado")

print("Buscando codigos....")
if re.search("27",codigo):
    print("Codigo encontrado")
else:
    print("Codigo no encontrado")
