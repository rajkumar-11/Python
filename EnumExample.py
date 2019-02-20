import enum
class Animal(enum.Enum):
    dog=1
    cat=2
    lion=3
print("The string representation of enum number is :",end="")
print(Animal.dog)

print("The repr representation of enum member is:",end="")
print(repr(Animal.dog))

print("The type of enum member is :",end=" ")
print(type(Animal.dog))

print("the name of enum member is :",end="")
print(Animal.dog.name)

print("All the enum values are :")
for anim in (Animal):
    print(anim)

di={}
di[Animal.dog]='bark'
di[Animal.lion]='roar'

if di=={Animal.dog :'bark',Animal.lion : 'roar'}:
    print("anum is hashed")
else:
    print("Enum is not hashed")

print("The enum member associated with value  2 is:",end="")
print(Animal(2))

print("The enum member associated with name lion is :",end=" ")
print(Animal['lion'])

mem=Animal.dog

print("The vlaue associated wiht dog is :",end="")
print(mem.value)

print("The name associted with dog is",end=" ")
print(mem.name)

if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")

if Animal.lion !=Animal.cat:
    print("Lions and cat are different")
else:
    print("Lion and cat are same")
























