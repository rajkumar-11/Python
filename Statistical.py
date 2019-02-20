import statistics

li=[1,2,2,2,3,3,3]

print("The average of list vlaues is ",end="")
print(statistics.mean(li))

print("The median of list elements is:",end="")
print(statistics.median(li))

print("the lower median of list element is :",end="")
print(statistics.median_low(li))

print("The higher median of list element is:",end="")
print(statistics.median_high(li))