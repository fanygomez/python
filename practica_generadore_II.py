#For anidados
def  devuelve_ciudades(*ciudades):
    for element in ciudades:
        #for subElement in element:
            yield  from element

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))