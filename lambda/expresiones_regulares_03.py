import re

# lista_nombres = [
#     'Ana',
#     'Fany',
#     'Cris',
#     'Sandra',
#     'Sebas'
# ]
lista_nombres = [
    'Ma1',
    'Se1',
    'Ma2',
    'Va1',
    'Va3',
    'Ma4',
    'MaA',
    'Ma.5',
    'MaB',
    'Ma:C'
]

for elemento  in lista_nombres:
    # if re.findall('[o-t]$', elemento):
    # if re.findall('Ma[0-3]', elemento): Ma1,M2
    # if re.findall('Ma[^0-3]', elemento): #^ negacion Ma4
    # if re.findall('Ma[^0-3]', elemento): #^ negacion Ma4
    # if re.findall('Ma[0-3A-B]', elemento): #^ negacion Ma4
    if re.findall('Ma[.:]', elemento): #^ negacion Ma.5,Ma:C
        print(elemento)
