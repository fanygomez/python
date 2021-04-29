class Coche():
    def desplazamiento(self):
        print("Me desplazo utitlizando cuadro ruedas")

class Moto():
    def  desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def  desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#Instancias
miVehiculo =Moto();
#miVehiculo.desplazamiento()
desplazamientoVehiculo(miVehiculo)
miVehiculo2 =Coche();
#miVehiculo2.desplazamiento()
desplazamientoVehiculo(miVehiculo2)
miVehiculo3 =Camion();
#miVehiculo3.desplazamiento()
desplazamientoVehiculo(miVehiculo3)