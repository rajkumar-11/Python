import time,calendar,cmath,random
from fractions import Fraction

# print(calendar.calendar(2012,4,2,14))
x=-1.0
y=0
z=complex(x,y)
print("the phase of complex number is : ",end="")

print("random number generated here is %s" % (random.random()))

print(" A random number form list is :",end=" ")
print(random.choice([3,2,4,5,1]))

print(" A random number from range is :",end=" ")
print(random.randrange(20,50,3))


print(Fraction(11,35))
print(Fraction(10,18))
print(Fraction(1.13))
print(Fraction('1.13'))
print(Fraction('3.14159265358979323846').limit_denominator(10000000))