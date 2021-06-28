#Agregar funcionalidad  imprimit antes y despues de mostrar el resultado
# def funcion_decararadoraA(funcion_parametroB):
#arg numero indefinod de parameteos
def funcion_decararadoraA(funcion_parametroB):
    # def funcion_interiorC(*args):
    #** kwargs: paramtros clave valor
    def funcion_interiorC(*args, **kwargs):
        #Acciones decoradoras
        print("Se realizara el calculo: ")
        funcion_parametroB(*args, **kwargs)
        print("Hemos terminado el cálculo")
    return funcion_interiorC
#@Nombre de funcion decoradora

@funcion_decararadoraA
def suma(num1,num2):
    print(num1+num2)
@funcion_decararadoraA
def resta(num1,num2):
    print(num1-num2)
@funcion_decararadoraA
def potencia (base,exponente):
    print(pow(base,exponente))
print("Test...")
suma(20,20)
resta(30,10)
#argumetnos con clave valor
potencia(base=5,exponente=3)