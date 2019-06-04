def findLIS(arr,n):
    temp=[0 for i in range(n)]

    temp[0]=arr[0]
    len=1

    for i in range(n):
        if arr[i]<temp[0]:
            temp[0]=arr[i]
        elif arr[i]>temp[len-1]:
            temp[len]=arr[i]
            len+=1
        else:
            temp[findIndex(temp,arr[i],-1,len-1)]=arr[i]

    return len


def findIndex(temp,value,l,r):
    while(r-l>1):
        mid=l+(r-l)//2
        if temp[mid]>=value:    
            r=mid
        else:
            l=mid

    return r




if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    # print(arr)
    length=findLIS(arr,n)
    print(length)