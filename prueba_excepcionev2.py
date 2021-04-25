def dividir():
    try:
        num1 = (float(input("Introduce el primer numero: ")))

        num2 = (float(input("Introduce el segundo numero: ")))
        print("La divisiòn es: "+ str(num1/num2))
    except ValueError:
        print("El valor introducido no es valido")
    except ZeroDivisionError:
        print("No es posible dividir entre 0")
    #Siempre se ejecutara
    finally:
        print("Calculo finalizado...")
dividir()