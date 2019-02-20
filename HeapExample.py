import heapq

li=[5,7,9,1,3]

heapq.heapify(li)

print("The created heap is :",end="")

print(list(li))

heapq.heappush(li,4)

print("The modified heap after push is:",end="")
print(list(li))

print("The popped and smallest element is :",end="")

print(heapq.heappop(li))


l1=[5,7,9,4,3]
l2=[5,7,9,4,3]

heapq.heapify(l1)
heapq.heapify(l2)

print("The popped item using heappushpop() is ",end="")
print(heapq.heappushpop(l1,2))

print("The popped item using heaperplace is :",end=" ")
print(heapq.heapreplace(l2,2))


list=[6,7,9,4,3,5,8,10,1]

heapq.heapify(list)

print("The 3 largest number in list are",end=" ")
print(heapq.nlargest(3,list))

print("The 3 smallest numbers in the list are :",end="")
print(heapq.nsmallest(2,list))