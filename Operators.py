import operator

a,b=10,20

min=a if a<b else b
print(min)

print("a is equal to b" if a==b else "a is greater than b " if a>b else "b is greater than a")
a=a+1
print(a/2)

list=[1,2,2,4]
operator.iadd(list,[4,3,5])
print(list)

operator.setitem(list,3,3)
print(list)