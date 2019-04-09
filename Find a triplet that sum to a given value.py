
def find3Numbers(A,n,sum):

    for i in range(0,n-1):
        tempsum=sum-A[i]
        s=set()
        for j in range(i+1,n):
            if tempsum-A[j] in s:
                print("yes")
                return
            s.add(A[j])



if __name__=="__main__":
    A = [1, 4, 45, 6, 10, 8]
    sum = 22
    arr_size = len(A)
    find3Numbers(A, arr_size, sum)