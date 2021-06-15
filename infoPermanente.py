import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una nueva persona con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = [];

    def __init__(self):
        listaDePersonas = open("ficheroExternoP.txt", "ab+")
        # Mover el puntero al finally
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del listaDePersonas

    def agregarPersonas(self, p):
        self.personas.append(p)

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def agregarPersonasEnFicheroExt(self):
        listaDePersonas = open("ficheroExternoP.txt", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del listaDePersonas

    def mostrarInfoFicheroExt(self):
        print("La infomacion del fichero externo es la siguiente")
        for p in self.personas:
            print(p)


# Instancias
miLista = ListaPersonas()

persona = Persona("Sandra", "Femenino", 45)
miLista.agregarPersonas(persona)
miLista.agregarPersonasEnFicheroExt()
miLista.mostrarInfoFicheroExt()
# persona = Persona("Ale","Masculino",2)
# miLista.agregarPersonas(persona)
# miLista.guardarPersonasEnFicheroExt()
# persona = Persona("Dilan","Masculino",1)
# miLista.agregarPersonas(persona)
# print("Lista")
# miLista.mostrarPersonas()
