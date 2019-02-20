class Person(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

emp=Person("Geek1")
print(emp.getName(),emp.isEmployee())

emp2=Employee("Geek2")
print(emp2.getName(),emp2.isEmployee())

print(issubclass(Employee,Person))
print(issubclass(Person,Employee))

print(isinstance(emp2,Person))
print(isinstance(emp,Employee))