import pickle
from modulo_vehiculo import *
coche1 = Vehiculo("Mazda", "MX5")
coche2 = Vehiculo("Seata", "Leon")
coche3 = Vehiculo("Renault", "Megane")

coches =[ coche1,coche2,coche3];

fichero = open("coches","wb")

#Volcado de datos
pickle.dump(coches,fichero)

fichero.close()

del(fichero)

ficheroApertura = open("coches","rb")
miscoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscoches:
    print(c.estado())