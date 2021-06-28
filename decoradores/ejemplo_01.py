#Agregar funcionalidad  imprimit antes y despues de mostrar el resultado
def funcion_decararadoraA(funcion_parametroB):
    def funcion_interiorC():
        #Acciones decoradoras
        print("Se realizara el calculo: ")
        funcion_parametroB()
        print("Hemos terminado el cálculo")
    return funcion_interiorC
#@Nombre de funcion decoradora

@funcion_decararadoraA
def suma():
    print(15+20)
@funcion_decararadoraA
def resta():
    print(30-10)

print("Test...")
suma()
resta()