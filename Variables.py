from functools import *
a=3
b=9
if b%a==0:
    print("b is divisible by a")


def div(a,b):
    if(b%a==0):
        print("yes b is divisible by a")
    else:
        print(" b is  not divisible by a")

div(5,5)

m=((1,2),(3,4),(5,6))

for row in m:
    print(row)

print(len(m))

#rez=((m[j][i] for j in range(len(m)) )for i in range(len(m[0])))
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

for row in rez:
    print(row)

print("\n")
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
transpose_matrix=zip(*matrix)
for row in transpose_matrix:
    print(row)



a=10

def f():
    print(s)
    #s = "Me too."

s = "I love Geeksforgeeks"
f()

print (s)

def add(a,b,c):
    return 100*a+10*b+c

add_part=partial(add,c=2,b=1)

print(add_part(3))



def function(a,b,c,d):
    print(a,b,c,d)
my_list=[1,2,3,4]
function(*my_list)


def mySum(*args):
    sum=0
    args=list(args)
    args[0]=99
    for i in range(0,len(args)):
        sum=sum+args[i]
    return sum;

print(mySum(1,2,2,3))
print(mySum(1,2,2,3,4,3,5))

a='0110'
print(int(a,2))





















