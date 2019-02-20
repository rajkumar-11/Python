class Person:
    def __init__(self):
        print("our class is created")
    def __del__(self):
        print("class instance is destroyed")
    def setFullname(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def printFullName(self):
        print(self.firstName,self.lastName)

PersonName=Person()
PersonName.setFullname('rajkumar','navhal')
PersonName.printFullName()


class Employee(Person):
    pass

employee= Employee()
employee.setFullname('ramesh','sharma')
print(employee.firstName)
print(employee.lastName)