#raise ZeroDivisionError("")
import math
def  calcularRaiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

num1 = (int(input("Introduce un nùnmero: ")))
try:
    print(calcularRaiz(num1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)