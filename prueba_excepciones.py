def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No es posible dividir entre 0")
        return "Operacion no valida"
while True:
    try:
        op1 = (int(input("Introducir primer numero: ")))
        op2 = (int(input("Introducir segundo numero: ")))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo!")

operacion = input("Introducir la operación a realizar ( suma, resta, multiplicar, dividir) : ")

if operacion=="suma":
    print(suma(op1,op2))
elif operacion =="resta":
    print(resta(op1,op2))
elif operacion =="multiplicar":
    print(multiplicar(op1,op2))
elif operacion =="dividir":
    print(dividir(op1,op2))
else :
    print("Operacion no valida")


print("Operacion ejecutada....")