

def getCount(k,s1,s2):
    l=len(s1)
    temp=[[0 for i in range(l+1)] for j in range(l+1)]
    for i in range(1,l+1):
        for j in range(l,l+1):
            if s[i-1]==s[j-1]:
                





if __name__=="__main__":
    t=int(input())
    for i in range(t):
        l=list(input().split())
        k=int(list[0])
        count=getCount(k,list[1],list[2])