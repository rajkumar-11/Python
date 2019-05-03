if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, g = map(int, input().split())
        arr = list(map(int, input().split()))
        # print(arr)

        # if n == 1:
        #     if arr[0] > g:
        #         print("NO")
        #     else:
        #         print("YES")
        # else:
        #     arr.sort(reverse=True)
        #     l1 = arr[0]
        #     l2 = arr[1]
        #     index = 2
        #     i = 0
        #     flag = True
        #     while (i <= g):
        #         if l1 == 0 and l2 == 0:
        #             print("YES")
        #             flag = False
        #             break
        #         minValue = min(l1, l2)
        #         if l1 == 0:
        #             if l2 + i <= g:
        #                 print("YES1")
        #                 flag = False
        #                 break
        #             else:
        #                 print("NO1")
        #                 flag = False
        #                 break
        #         elif l2 == 0:
        #             if l1 + i <= g:
        #                 print("YES2")
        #                 flag = False
        #                 break
        #             else:
        #                 print("NO2")
        #                 flag = False
        #                 break
        #
        #         if i + minValue > g:
        #             print("NO3")
        #             flag = False
        #             break
        #         else:
        #             l1 = l1 - minValue
        #             l2 = l2 - minValue
        #             if l1 == 0:
        #                 if (index > n - 1):
        #                     print("NO4")
        #                     flag = False
        #                     break
        #                 l1 = arr[index]
        #                 index = index + 1
        #             elif l2 == 0:
        #                 if (index > n - 1):
        #                     print("NO5")
        #                     flag = False
        #                     break
        #                 l2 = arr[index]
        #                 index = index + 1
        #         i = i + minValue
        #         # print("i= ", i)
        #
        #     if flag == True:
        #         print("NO6")
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
        temp=[[False for  i in range(sum+1)]for j in range(n+1)]
        # print()
        # print(temp)
        for j in range(n+1):
            temp[j][0]=True

        for i in range(1,n+1):
            for j in range(1,sum+1):
                temp[i][j]=temp[i-1][j]
                if j>=arr[i-1]:
                    temp[i][j]=temp[i][j]or temp[i-1][j-arr[i-1]]

        diff=999999999999999
        tempsum=0
        for j in range(sum//2,0,-1):
            if temp[n][j] is True:
                diff=sum-2*j
                tempsum=j
                break
        x=sum-2*tempsum
        if(x+tempsum<=g):
            print("YES")
        else:
            print("NO")




