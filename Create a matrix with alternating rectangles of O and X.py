
def fill0X(Row,Col):
    T = 0
    B = Row - 1
    L = 0
    R = Col - 1
    Arr=[[ 2 for i in range(Col)] for j in range(Row)]
    x=0;
    A=['X','0']

    while (T <= B and L <= R):
        for i in range(L,R+1):
            Arr[T][i]=A[int(x%2)]
        T=T+1

        # if(T>B):
        #     break;

        for i in range(T,B+1):
            Arr[i][R]=A[x%2]
        R=R-1

        if(L<=R):
            for i in range(R,L-1,-1):
                Arr[B][i]=A[int(x%2)]
            B=B-1
        # print()

        if(T<=B):
            for i in range(B,T-1,-1):
                # print(L," ",i)
                Arr[i][L]=A[int(x%2)]
            L=L+1
        x=x+1

    for i in range(Row):
        for j in range(Col):
            print(Arr[i][j],end=" ")
        print()



if __name__=="__main__":
    print("Output for m = 10, n = 10")
    fill0X(10, 10)

    print("Output for m = 4, n = 4")
    fill0X(4, 4)

    print("Output for m = 3, n = 4")
    fill0X(3, 4)