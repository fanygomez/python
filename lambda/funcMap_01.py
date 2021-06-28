from flter_02 import *  # incluir todo lo que esta modulo

ListEmpleados = [
    Empleado("Sandra", "Director", 6700),
    Empleado("Fany", "Programador", 1950),
    Empleado("Alejandro", "Diseñador", 1800)
]

def calculo_comision(empleado):
    if( empleado.salario <= 3000):
        empleado.salario = empleado.salario * 1.03
        return empleado

listaEmpleadosMap = map(calculo_comision,ListEmpleados)
for emp in listaEmpleadosMap:
    print(emp)