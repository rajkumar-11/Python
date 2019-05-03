def getMinimumNumberOfChanges(arr,x):
   ans=99999999999
   minValue=min(arr)
   for i in range(5):
       ops=0
       for j in range(x):
           t=int(arr[j])-int(minValue-i)
           ops+=t//5+t%5//2+t%5%2
       ans=min(ops,ans)
   return ans




if __name__=="__main__":
    t=int(input())
    for  i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        # print(arr)
    a=getMinimumNumberOfChanges(arr,n)
    print(a)


