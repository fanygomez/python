'''
Metacaracteres ( carcateres comodin)
- Anclas y clases de caracteres
'''
import re

lista_nombres = [
    "Sandra Gomez",
    "Stefhanie Gomez",
    "Ale Guevara",
    "Leo Sorto"
]

for elemento in lista_nombres:
    # if re.findall('^Gomez',elemento):
    if re.findall('Gomez$',elemento):
        print(elemento)