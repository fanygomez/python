class Coche():
    #Estado inicial de los objeto
    #Constructor
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis= 250
        self.__ruedas = 4 #__ Encapsular esta propiedad con 2 guiones bajos (__), es accesible solo desde la clase
        self.__enmarcha = False
    def arrancar(self,estado):
        self.__enmarcha = estado
        if self.__enmarcha:
            check = self.__check_interno()
        if self.__enmarcha and check :
            return  'En marcha...'
        elif self.__enmarcha and check == False:
            return  'Algo ha ido mal en el check. No es posible arrancar el coche'
        else:
            return "Detenido"
    def estado(self):
        print("El coche tiene ",self.__ruedas,". Un ancho ",self.__anchoChasis)

    def __check_interno(self):
        print("Relizando check...")
        self.gasolina = 'ok'
        self.aceite = 'mal'
        self.puertas = 'cerradas'

        if self.gasolina=='ok' and self.aceite=='ok' and self.puertas=='ok':
            return True
        else:
            return False
        print("end check...")
#Ejemplarzar la clase, crear objeto, crear instancia
miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()
#Instancia 2
print("Obj2")
miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()