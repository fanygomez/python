#Def generarNumeros():
#   yeild numeros

def generaPares(limite):
    num = 1

    milista=[]

    while num<limite:
        milista.append(num*2)

        num = num + 1

    return milista

print(generaPares(10))

def generaParesv2(limite):
    num = 1
    while num<limite:
        yield num*2
        num = num + 1

devuelvePares = generaParesv2(10)

for i in devuelvePares:
    print(i)