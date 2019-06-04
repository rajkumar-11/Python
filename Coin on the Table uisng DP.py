if __name__ == "__main__":
    n, m, K = list(map(int, input().split()))
    x = -1
    y = -1
    arr=[[None for j in range(m)] for i in range(n)]
    for i in range(n):
       arr[i]=input()
       for j in range(m):
           if arr[i][j]=='*':
               x=i
               y=j
    # print("x= ",x," y= ",y)

    temp=[[[0 for x in range(m)] for j in range(n)] for i in range(K+1)]
    # print(temp)
    temp[0][0][0]=0

    for k in range(K+1):
        for i in range(n):
            for j in range(m):
                if k==0:
                    temp[k][i][j]= 0 if i is 0 and j is 0 else 999999999
                    # print(temp[k][i][j])
                else:
                     res=999999999
                     if i>0:
                         res=min(res,temp[k-1][i-1][j]+ (0 if arr[i-1][j]=='D' else 1))

                     if i<n-1:
                         res=min(res,temp[k-1][i+1][j]+ (0 if arr[i+1][j]=='U' else 1))

                     if j>0:
                         res=min(res,temp[k-1][i][j-1]+ (0 if arr[i][j-1]=='R' else 1))

                     if j<m-1:
                         res=min(res,temp[k-1][i][j+1]+ (0 if arr[i][j+1]=='L' else 1) )

                     temp[k][i][j]=res

    ans=999999999

    for k in range(K+1):
        ans=min(ans,temp[k][x][y])
    if ans!=999999999:
        print(ans)
    else:
        print(-1)



