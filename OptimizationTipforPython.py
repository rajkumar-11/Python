import  time

start=time.clock()

s="rajkumr"
U=[]
for c in s:
    U.append(c.upper())

elapsed=time.clock()
e1=elapsed-start
print(" time spent in function is ",e1)

start=time.clock()
U=map(str.upper,s)
elapsed=time.clock()
e2=elapsed-start
print(" Time spent in builtin function is:",e2)
