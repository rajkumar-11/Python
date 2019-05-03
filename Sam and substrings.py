
def FindSumOfAllSubstrtings(s):
    res=0
    f=1
    l=len(s)
    for i in range(l-1,-1,-1):
        # print(ord(s[i])-ord('0'))
        res=(res+(ord(s[i])-ord('0'))*f*(i+1))%1000000007
        f=(f*10+1)%1000000007
    return res




if __name__=="__main__":
    s=input()
    sum=FindSumOfAllSubstrtings(s)
    print(sum)