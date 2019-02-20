import numpy as np

arr=np.array([[1,2,4],[5,8,7]],dtype='float')
print ("Array created using passed list:\n", arr)

b=np.array((1,2,3))
print("Array created using passed tuple",b)

c=np.zeros((3,4))

print("Array initialized with all zeros",c)

d=np.full((3,3),6,dtype='complex')
print("\n An Array initialized with all 6s. Array type is complex:\n",d)

e=np.random.random((2,2))

print("\n A randdom array",e)

f=np.arange(0,30,5)

print("\n A sequential array with steps of 5:\n",f)

g=np.linspace(0,5,10)

print("\n A sequential array with 10 values between 0 and 5 \n",g)


h=np.array([[1,2,3],[4,5,6],[7,8,9]])

newarr=h.reshape(1,9)

print("\n original array \n",h)
print("Reshaped array \n",newarr)

flatten=h.flatten()

print("flattened array= ",flatten)


a=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])

temp=a[:2,::2]

print("\n Array wiht first 2 rows and alternate colums (0 and 2) \n",temp)

temparr=a[[0,1,2,3],[3,2,1,0]]

print("\n Elements at indices (0,3,(1,2),(2,1),(3,0 :\n",temp)

cond =a>0

temparr2=a[cond]

print(" \n elements greater than 0 :\n",temparr2)


arr1=np.array([1,2,5,3])

print("adding 1 to every element",arr1+1)

print("substracting 3 from each element ",arr1-3)

print(" Multiplying each element by 10",arr1*10)

print(" squaring each elment",arr1**2)

arr1=arr1*2

print("doubled each element of original array",arr1)

print("printing the transpose of the array",arr1.T)


arr2=np.array([[1,5,6],[4,7,2],[3,1,9]])

print("Largest element is:",arr2.max())

print("Row wise maximum elements:",arr2.max(axis=1))


print("colum wise minimum element ",arr2.min(axis=0))

print("sum of all array elements:",arr2.sum())


print("cummulative sum along each row \n",arr2.cumsum(axis=1))


a1=np.array([[1,2],[3,4]])
a2=np.array([[4,3],[2,1]])

print("Array sum: \n",a1+a2)

print("Array multiplication \n",a1*a2)

print("Matrix multiplication \n",a1.dot(a2))


q=np.array([0,np.pi/2,np.pi])

print("Sine values of array elements :",np.sin(q))

w=np.array([0,1,2,3])

print("exponent of array elements :",np.exp(w))

print("square root of array elements :",np.sqrt(w))

p=np.array([[1,4,2],[3,4,6],[0,-1,5]])

print("Array elements in sorted order",np.sort(p,axis=None))

print("Row wise sorted array",np.sort(p,axis=1))

print("Column wise sort by applying merge-sort",np.sort(p,axis=0,kind="mergesort"))

dtypes=[("name","S10"),("grad_year",int),("cgpa",float)]

values=[("Hrithik",2009,8.5),("ajay",2008,8.7),("pankaj",2008,7.9),("aakash",2009,9.0)]


av=np.array(values,dtype=dtypes)
print("\n Array sorted by names: \n",np.sort(av,order='name'))

print("aaat sorted by graduation year and then cgpa:\n",np.sort(av,order=['grad_year','cgpa']))

s1=np.array([[1,2],[3,4]])
s2=np.array([[5,6],[7,8]])


print("Vertical Stacking: \n",np.vstack((s1,s2)))

print("Horizontal Stacking :\n",np.hstack((s1,s2)))

s3=[5,6]

print("\n Column stacking :",np.column_stack(s3))


print(" Concatenation to 2nd axis : \n",np.concatenate((s1,s2),1))

print("\n\n\n splitting \n")

a6=np.array([[1,3,5,7,9,11],[2,4,6,8,12]])

print("Splitting along horizontal axis into 2 parts :\n",np.hsplit(a6,2))

print("splitting along vertical axis into 2 parts : \n",np.vsplit(a,2))

x=np.array([1.0,2.0,3.0])

z=2.0
print(x*z)

y=[2.0,2.0,2.0]

print(x*y)


print("\n\n\n\n")

x1=np.array([0.0,10.0,20.0,30.0])
y1=np.array([0.0,1.0,2.0])

print(x1[:,np.newaxis]+b)

print("\n working with date time\n\n")

today=np.datetime64('2017-02-12')

print('Date is :',today)

print('Year is :',np.datetime64(today,'Y'))


dates=np.arange('2017-02','2017-03',dtype='datetime64[D]')
print("\n dates of feb \n ",dates)
print("today is feb:",today in dates)


dur=np.datetime64('2017-05-22')-np.datetime64('2016-05-22')
print("\n No od days:",dur)
print("no of weeks:",np.timedelta64(dur,'W'))

ds=np.array(['2017-02-12','2016-10-13','2009-05-22'],dtype='datetime64')
print("\n Dates in sorted order",np.sort(ds))


print("linear algebra in Numpy \n\n\n")

matrix=np.array([[6,1,1],[4,-2,5],[2,8,7]])

print("Rank of A:",np.linalg.matrix_rank(matrix))

print("\nTrace of A:", np.trace(matrix))

print("\nDeterminant of A:", np.linalg.det(matrix))

print("\nInverse of A:\n", np.linalg.inv(matrix))

print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(matrix, 3))














































