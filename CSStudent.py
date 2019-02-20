class CSStudent:
     stream='cse'

     def __init__(self,roll):
         self.roll=roll

     def setAddress(self,address):
         self.address=address
     def getAddress(self):
         return self.address

a=CSStudent(101)
b=CSStudent(102)
a.setAddress("pune,Maharastra")

print(a.stream)
print(b.stream)
print(a.roll)
print(b.roll)
print(CSStudent.stream)

print(a.getAddress())