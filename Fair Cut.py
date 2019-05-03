

def getMinimumDiff(arr,n,k):
    if 2*k>n:
        k=n-k
    s1=""
    arr.sort()
    for i in range(k):
        s1=s1+"10"
    a=(n-2*k)//2
    b=n-a-2*k
    for i in range(b):
        s1=s1+"0"

    for  i in range(a):
        s1="0"+s1
    # return s1
    result=0
    set1=[]
    set2=[]
    for i in range(n):

        if s1[i]=='1':
            set2.append(arr[i])
        else:
            set1.append(arr[i])

    # print(set1)
    # print(set2)

    return diff(set1,set2)


def diff(set1,set2):
    result=0
    for i in range(len(set1)):
        for j in range(len(set2)):
            result=result+abs(set1[i]-set2[j])
    return result





if __name__=="__main__":
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))

    x=getMinimumDiff(arr,n,k)
    print(x)
