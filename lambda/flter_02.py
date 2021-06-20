class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $" \
            .format(self.nombre, self.cargo, self.salario)


ListEmpleados = [
    Empleado("Sandra", "Director", 75000),
    Empleado("Fany", "Programador", 1200),
    Empleado("Alejandro", "Diseñador", 1000)
]
salarios_altos = filter(lambda empleado:empleado.salario > 1000,ListEmpleados)
for emp in salarios_altos:
    print(emp)