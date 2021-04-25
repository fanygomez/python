class Person():
    def __init__(self,name,age,location):
        self.name = name;
        self.age = age;
        self.location = location;
    def description(self):
        print("Name: ",self.name,"Age: ",self.age,"Location : ",self.location)
#Employee herada de la clase persona
class Employee(Person):
    def __init__(self, salary,antiguedad,name_person,age_person,location_person):
        super().__init__(name_person,age_person,location_person)
        self.salary = salary;
        self.antiguedad = antiguedad;
    def description(self):
        super().description()
        print("salary: ",self.salary,"antiguedad: ",self.antiguedad)
person = Person("Antonio",8,"SV")
employee = Employee(1500,8,"Antonio",8,"SV")
person.description()
employee.description()
#Proncipio de sustitucion
#Un empleado siempre sera una persona
#Una persona no siempre sera un empleado
print(isinstance(employee,Person))
print(isinstance(person,Employee))
