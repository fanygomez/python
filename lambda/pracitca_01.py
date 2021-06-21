#Funciones lambda
def area_triangulo(base,altura):
    return (base*altura)/2

area_traianguloLambda = lambda base,altura:(base  * altura) /2
print(area_traianguloLambda(7,5))
print(area_traianguloLambda(9,6))
print("AL CUBO")
al_cubo1 = lambda numero:numero**3
print(al_cubo1(13))
al_cubo = lambda numero:pow(numero,3)
print(al_cubo(13))