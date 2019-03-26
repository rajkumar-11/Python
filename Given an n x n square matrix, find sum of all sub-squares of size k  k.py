def printSumSimple(mat,k):
    m = len(mat)
    n = len(mat[0])
    print(m, " ", n)
    ans=[[-1 for i in range(m-k+1)] for j in range(n-k+1)]
    # print(ans)
    if(k>m or k>n):
        return "Not possible"
    sum=0
    for i in range(k):
        for j in range(k):
            sum+=mat[i][j]
    a=0
    b=0
    sumouter=sum;

    for i in range(k-1,m):
        # print("here")
        if(i>=k):
            for x in range(0,k):
                sumouter=sumouter+mat[i][x]-mat[i-k][x]
            sum=sumouter;
        ans[a][b]=sumouter;
        b=b+1

        for j in range(k,n):
            for q in range(0,k):
                sum+=mat[a+q][j]-mat[a+q][j-k]
            ans[a][b]=sum;
            b=b+1
        a=a+1
        b=0
    print(ans)


if __name__ == "__main__":

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    k = 3
    printSumSimple(mat, k)