for i in [2,3,4,5]:
    print("hola: ")

email = False
for i in "gmzgmail.com":
    if (i == "@"):
        email = True
if email ==True:
    print("Email correcto")
else:
    print("El email no es correcto")

miEmail = input("Introdusca su email: ")
contador = 0
for i in miEmail:
    if (i == "@" or i == "." ):
        contador = contador +1
        print(contador)
if contador > 1:
    print("Email correcto")
else:
    print("El email no es correcto")

#py 3 -> renge(n) crea un arrays de n elementos
for i in range(5):
    print(i)
    print(f" El valor de la variable {i}")