from modulo_vehiculo import *

#Instancias
print("Moto")
miMoto = Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()
print("Furgoneta")
mifurgoneta = Furgoneta("Renault","Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))

print("Bicileta")
miBici = BicicletaElectrica("Orbea","Kangoo")