

def getTheNumber(s,n):
    left=0
    right=0
    minValue=999999
    dict={'A':0,'C':0,'T':0,'G':0 }
    for i in range(n):
        dict[s[i]]=dict[s[i]]+1
    # while(right<n-1):
    # print(dict)
    while(right<n-1):
        dict[s[right]]=dict[s[right]]-1
        right=right+1
        while(isBalanced(dict,n)):
            minValue=min(minValue,right-left)
            dict[s[left]]=dict[s[left]]+1
            left=left+1

    return minValue


def isBalanced(dict,n):
    value=n//4
    if dict['A']<=value and dict['T']<=value and dict['G']<=value and dict['C']<=value:
        return True
    return False





if __name__=="__main__":
    n=int(input())
    s=input()
    result=getTheNumber(s,n)
    print(result)