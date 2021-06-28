import pickle

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
