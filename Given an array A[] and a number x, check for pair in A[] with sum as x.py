
def printPairs(A,len,n):
    A.sort()
    i=0
    j=len-1
    while(i<j):
        if A[i]+A[j]==n:
            print("Pair with given sum ",n," is (",A[i],A[j],")")
            return
        elif A[i]+A[j]>n:
             j=j-1
        else:
            i=i+1


if __name__=="__main__":
    A = [1, 4, 45, 6, 10, 8]
    n = 16
    printPairs(A, len(A), n)