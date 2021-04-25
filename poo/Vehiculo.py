#Herencia
class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelara = False
        self.frena = False
    def arrancar(self):
        self.enmarcha = True

    def acelar(self):
        self.acelara = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca; ", self.marca,"\n Modelo: ", self.modelo,"\n En marcha: ",self.enmarcha)
#Herencia
class Furgoneta(Vehiculo):
    def carga(self,carga):
        self.cargado = carga

        if( self.cargado):
            return "La furgoneta esta cargada!"
        else:
            return "La furgoneta no esta cargada"
class Moto(Vehiculo):
    hcaballito  = ""
    def caballito(self):
        self.hcaballito = "Test"
    #Sobreescribir metodo
    def estado(self):
        print("\n Marca ", self.marca,"\n Modelo: ", self.modelo,"\n En marcha: ",self.enmarcha,"\n ",self.hcaballito)

class VElectricos(Vehiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargando = True
#Herencia Multiple
#Herada el constructor la primera clase especificada a la izquierda (VElectricos)
#Los metodos con el mismo nombre seran herados de VElectricos
# Y el resto de metodos  todos seran heredados de ambas clases
#uso super() -> Llamara a la clase padre (llama al metodo padre)
# uso de isInstance()
#
class BicicletaElectrica(VElectricos,Vehiculo):
    pass

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
