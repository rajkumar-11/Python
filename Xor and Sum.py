import os
import sys

def xorAndSum(a, b):


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
