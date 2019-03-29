BITTree= [0]*1000


def constructBITree(arr,n):

     for i in range(n):
         updatebit(i,n,arr[i])

def updatebit(i,n,val):
    i+=1
    while i<=n:
        BITTree[i]+=val
        i=i+(i&-i)

def update(l,r,n,val):
    updatebit(l,n,val)
    updatebit(r,n,-val)

def getSum(i):
    sum=0;
    while(i>0):
        sum+=BITTree[i]
        i=i-(i&-i)
    return sum



if __name__=="__main__":
    arr=[0]*5
    n=len(arr)
    constructBITree(arr,n)
    l=2
    r=4
    val=2
    update(l,r,n,val)
    index=4
    print("element at index ",index," is ",getSum(index))
    l=0
    r=3
    val=4
    update(l,r,n,val)
    index=3
    print("element at index ", index, " is ", getSum(index))

