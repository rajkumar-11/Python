import keyword

for x in range(1,5):
    print(x)

if keyword.iskeyword("if"):
    print("yes")

    print("these are the keywords")
    print("The list of keywords is : ")
    print(keyword.kwlist)

print(False==0)
print(True==0)
print(True+True+True)
print(not False)

x=None
y=None
a=[1,2,3]
print(a)
del a[2]
print(a)
assert 5 > 3, "5 is not smaller than 3"

if 'k' in 'rajkumar':
    print(" k is part of rajkumar")
else: print("k is not a part of rajkumar")

for i  in 'mahima':
    print(i,end="\t")

print(" Value of a using nonlocal is : ",end=" ")

def outer():
    a=5
    def inner():
        nonlocal a
        a=10
    inner()
    print(a)

outer()
