def spiralPrint(R,C,a):
    T=0
    B=R-1
    L=0
    R=C-1
    while(T<=B and  L<=R):

        # if(L>R):
        #     break;
        for i in range(L,R+1):
            print(a[T][i],end=" ")
        T=T+1

        # if(T>B):
        #     break;

        for i in range(T,B+1):
            print(a[i][R],end=" ")
        R=R-1

        if(L<R):
            for i in range(R,L-1,-1):
                print(a[B][i],end=" ")
            B=B-1
        # print()

        if(T<B):
            for i in range(B,T-1,-1):
                # print(L," ",i)
                print(a[i][L],end=" ")
            L=L+1
        # print()
        # print("L= ",L," R= ",R," T= ",T," B= ",B)


if __name__=="__main__":
    a = [[1, 2, 3,4,5,6],
         [7,8,9,10,11,12],
         [13,14,15,16,17,18],
         [19,20,21,22,23,24],
         [25,26,27,28,29,10],
         [31,32,33,34,35,36]]

    R = 6
    C = 6
    spiralPrint(R, C, a)