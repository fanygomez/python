#imporrtar
from modulos import funciones_math
class Areas:
    """ Esta clase calcula las áreas de diferentes figuras geométricas"""
    def areaCuadrado(lado):
        """ Calula el area de una cuadrado elevando al cuadrado el lado por parametro """
        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base,altura):
        return "El área del tringulo es: " + str((base * altura)/2)

# print(Areas.areaCuadrado(5))
#Mostrando cometarios en tiempo de Ejecucion de la funcion ( .__doc__)
# print(areaCuadrado.__doc__
help(Areas)
# help(Areas.areaCuadrado)

#Mostrando documntacion de modulos
help(funciones_math)