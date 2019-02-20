import collections

Student=collections.namedtuple('Student',['name','age','DOB'])

S=Student("Nandini","19","2012321")

li=["Manjeet","19","411997"]

di={'name':"Nikhi",'age':19,'DOB':'122432'}

print("The nametuple instance using iterable is : ")

print(Student._make(li))

print("The OrderedDict instance using namedtuple is :")
print(S._asdict())

print("The namedtuple instance from dict is : ")
print(Student(**di))


s1=Student("Nandini",'19',"3424323")

print("All the fields of students are :")

print(s1._fields)

print("The modified namedtuple is:")
print(s1._replace(name="MANKJEET"))