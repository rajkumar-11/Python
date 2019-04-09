import math
def subsetXOR(arr,n,k):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    m=(1<<(int)(math.log2(max)+1))-1

    dp=[[0 for i in range(m+1)]for j in range(n+1)]
    dp[0][0]=1

    for i in range(1,n+1):
        for j in range(m+1):
            dp[i][j]=dp[i-1][j]+dp[i-1][j^arr[i-1]]

    return dp[n][k]




if __name__=="__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    n = len(arr)
    print("Count of subsets is",subsetXOR(arr, n, k))