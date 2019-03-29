
def getsum(BITree,i):
    sum=0
    i=i+1
    while(i>0):
        sum+=BITTree[i]
        i-=(i&-i)
    return sum

def updatebit(BITree,n,i,v):
     j=i+1
     while(j<=n):
         BITree[j]+=v
         j+=(j&-j)

def construct(arr,n):
    BITree= [0]*(n+1)
    for i in range(n):
        updatebit(BITree,n,i,arr[i])
    return BITree

if __name__=="__main__":
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    BITTree = construct(freq, len(freq))
    print("Sum of elements in arr[0..5] is " + str(getsum(BITTree, 5)))
    freq[3] += 6
    updatebit(BITTree, len(freq), 3, 6)
    print("Sum of elements in arr[0..5]" +
          " after update is " + str(getsum(BITTree, 5)))