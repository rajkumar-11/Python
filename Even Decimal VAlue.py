

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        s=input()
        count=0
        for i in range(n):
            # print("s[-1] ",s[-1])
            s=s[1:]+s[0]
            # print("s= ",s)
            x=int(s,2)
            if x%2==0:
                count+=1
        print(count)
