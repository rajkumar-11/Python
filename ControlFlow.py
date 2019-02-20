#from collections import Counter
import itertools
# import operator
# cars=["NANO","ALTO","I10","I20"]
# car=0
# while car < len(cars):
#     print(cars[car])
#     car+=1
#
# for x in enumerate(cars,start=1):
#     print(x[0],x[1])
#
# prices={1:"129000",2:"350000",3:"500000",4:"800000"}
#
# for index,x in enumerate(cars,start=1):
#     print("Car= %s Prics=%s"\
#           %(x,prices[index]))
#
# accessories=["GPS","Car Repair Kit","Dolby Sound Kit"]
# for c,a in zip(cars,accessories):
#     print("car: %s,Accessory required=%s"%(c,a))
#
# l1,l2=zip((*[('Aston','GPS'),('Audi','Car Repair'),('McLaren','Dolby Sound Kit')]))
# print(l1)
# print(l2)
#
# li1=[1,4,5,7]
# li2=[1,6,5,9]
# li3=[8,10,5,4]
# print("the sum after each iteration is :",end=" ")
# print(list(itertools.accumulate(li1)))
#
# print("the multiplied  after each iteration is :",end=" ")
# print(list(itertools.accumulate(li1,operator.mul)))
#
# print("all values in the mentioned chain are :",end=" ")
# print(list(itertools.chain(li1,li2,li3)))
# print("The compressed values in the string are:", end=" ")
# print(list(itertools.compress('Geeksforgeeks',[1,0,0,0,0,1,0,0,1,0,0,0,0])))
#
# li4=[li1,li2,li3]
# print(" All values in mentioned chain are : ", end=" ")
# print (list(itertools.chain.from_iterable(li4)))
# print("here")
#
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
# # for value in simpleGeneratorFun():
# #     print(value)
#
#
#
#
# def nextSquare():
#     i=1
#     while True:
#         yield i*i
#         i=i+1
#
# for num in nextSquare():
#     if num>100:
#         break
#     print(num,end=" ")
#
#
# print()
#
# y=simpleGeneratorFun()
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
#
#
# def fib(limit):
#     a,b=0,1
#     while a<limit :
#         yield a
#         a,b=b,a+b
#
# z=fib(5)
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
#
# print("using in loop")
#
# for i in fib(100):
#     print(i)
#
# list=[1,5,3,6,8,23,1,5,7,2,3]
# for i in sorted(list):
#     print(i,end=" ")
# print()
#
# for i in list:
#     print(i,end=" ")
# print()
#
# for i in reversed(sorted(set(list))):
#     print(i,end=" ")
#
# # Python code to demonstrate range() vs xrange()
# # on  basis of return type
#
# # initializing a with range()
# a = range(1, 10000)
#
#
# # testing the type of a
# # print("The return type of range() is : ")
# # print(type(a))
# #
# # A=map(int,input().split())
# # B=map(int,input().split())
# # print(*itertools.product(A,B))

# print()

s,k=input().split()
# for i in range(1,int(k)+1):
#     for j in itertools.combinations(sorted(s),i):
#         print("".join(j))
#






print(*["".join(i) for i in itertools.combinations_with_replacement(sorted(s),int(k))],sep="\n")




import itertools
s,k=input().split()
print(*["".join(i) for i in itertools.combinations_with_replacement(s,int(k))],sep="\n")












