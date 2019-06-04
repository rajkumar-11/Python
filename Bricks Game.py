def getMaximum(arr, n):
    temp = [0 for i in range(n)]
    sum=0
    if(n>=1):
        sum+=arr[n-1]
        temp[n-1]=sum

    if(n>=2):
        sum+=arr[n-2]
        temp[n-2]=sum

    if(n>=3):
        sum+=arr[n-3]
        temp[n-3]=sum
    i=n-4
    while(i>=0):
        sum=sum+arr[i]
        temp[i]=max(sum-temp[i+1],max(sum-temp[i+2],sum-temp[i+3]))
        i=i-1
    return temp[0]



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = getMaximum(arr, n)
        print(result)
