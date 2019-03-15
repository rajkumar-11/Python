
def printMaxSubSquare(M):
    R=len(M)
    C=len(M[0])
    max=0
    # print("Row= ",R," Col= ",C)
    Arr=[[0 for i in range(C+1)] for j in range(R+1)]
    # print(Arr)
    # print("length= ", len(Arr))
    for i in range(R+1):
        for j in range(C+1):
            if i==0 or j==0:
                # print("i= ",i," j= ",j)
                Arr[i][j]=0
                continue;
            if M[i-1][j-1]==1:
                x=min(Arr[i-1][j],min(Arr[i-1][j-1],Arr[i][j-1]))+1
                Arr[i][j]=x
                if x>max:
                    max=x
    print(max)



if __name__=="__main__":
    M = [[0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

    printMaxSubSquare(M)
