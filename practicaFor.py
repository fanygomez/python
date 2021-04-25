for i in range(5,50,3):
    print(i)
    print(f" El valor de la variable {i}")


miEmail = input("Introdusca su email: ")
contador = 0
for i in range(len(miEmail)):
    if (i == "@" or i == "." ):
        contador = contador +1
        print(contador)
if contador > 1:
    print("Email correcto")
else:
    print("El email no es correcto")