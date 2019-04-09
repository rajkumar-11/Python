def printMatrix(M):
    m=len(M)
    n=len(M[0])
    for i in range(m):
        for j in range(n):
            print(M[i][j],end=" ")
        print()


def diagonalOrder(M):
    m = len(M)
    n = len(M[0])
    for i in range(m):
        x=i
        y=0
        while(x>=0 and y<n):
            print(M[x][y],end=" ")
            x=x-1
            y=y+1
        print()
    for  j in range(1,n):
        x=m-1
        y=j
        while (x >= 0 and y < n):
            print(M[x][y], end=" ")
            x = x - 1
            y = y + 1
        print()


if __name__=="__main__":
    M = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16],
         [17, 18, 19, 20]]
    print("Given matrix is ")
    printMatrix(M)

    print("\nDiagonal printing of matrix is ")
    diagonalOrder(M)
