import sys

def multiplyAll(*values):
    mul=1
    print(values)
    print("Type=",type(values))

    for i in values:
        mul*=i

    return mul

answer=multiplyAll(1,2)
print("The Multiplication of 1 and 2 is ",answer)

answer=multiplyAll(3,4,5,6,7)
print("The multiplication of 3 to 7 is ",answer)


def printDetails(**details):
    print("Parameter details contain")
    print(details)
    print("Type=",type(details))

    print("First name=",details['firstname'])

    print("Department= ",details['department'])

    print("  ")

printDetails(firstname="Nikhil",rollno="007",department="CSE")
printDetails(firstname="Abhay",department="ECE")
