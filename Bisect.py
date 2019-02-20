import bisect

li=[1,3,4,4,4,6,7]


print(" The rightmist index to insert, so list remains sorted is :",end="")

print(bisect.bisect(li,4))

print("the left most index to insert, so list remains sorted is:",end="")

print(bisect.bisect_left(li,4))

print("the right most index to  insert so list remains sorted is",end="")

print(bisect.bisect_right(li,4,0,4))

bisect.insort_left(li,4)

print(li)