#Agregar funcionalidad  imprimit antes y despues de mostrar el resultado
# def funcion_decararadoraA(funcion_parametroB):
#arg numero indefinod de parameteos
def funcion_decararadoraA(funcion_parametroB):
    def funcion_interiorC(*args):
        #Acciones decoradoras
        print("Se realizara el calculo: ")
        funcion_parametroB(*args)
        print("Hemos terminado el cálculo")
    return funcion_interiorC
#@Nombre de funcion decoradora

@funcion_decararadoraA
def suma(num1,num2):
    print(num1+num2)
@funcion_decararadoraA
def resta(num1,num2):
    print(num1-num2)

print("Test...")
suma(20,20)
resta(30,10)