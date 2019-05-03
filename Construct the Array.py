#!G/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    F=[0 for i in range(n)]
    G=[0 for i in range(n)]
    F[2]=1
    G[2]=0
    for i in range(3,n+1):
        F[i]=G[i-1]+(k-2)*F[i-1]
        G[i]=(k-1)*F[i-1]
        F[i]=F[i]%1000000007
        G[i]=G[i]%1000000007

    if x==1:
        return G[n]
    else:
        return F[n]





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
