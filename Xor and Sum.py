import os
import sys

def xorAndSum(a, b):
    ans=0
    a=int(a,2)
    b=int(b,2)
    for i in range(314160):
        ans+=a^(b<<i)
        ans=ans%(1000000007)
    return ans



if __name__ == '__main__':
   a=input()
   b=input()
   result=xorAndSum(a,b)
   print(result)

        