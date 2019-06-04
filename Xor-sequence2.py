

def G(r):
    x=r%8
    if x==0 or x==1:
        return r
    elif x==2 or x==3:
        return 2
    elif x==4 or x==5:
        return r+2
    elif x==6 or x==7:
        return 0
    return 0



if __name__ == "__main__":
    q = int(input())

    for i in range(q):
        l = list(map(int, input().split()))
        r = l[0]
        s = l[1]
        ans=G(s)^G(r-1)
        print(ans)

