from math import log,ceil


def canBeExpressedAsPower(n):

    i=2
    while(i*i<=n):
        x=log(n)/log(i)
        print("i= ",i)
        print("int(x)=",ceil(x))
        print("x= ",x)
        print("abs= ",abs(ceil(x)-x))
        if(abs(ceil(x)-x)<0.000001):
            return True
        i+=1

    return False



if __name__ == "__main__":
    n = int(input())
    if (canBeExpressedAsPower(n)):
        print("Yes it can be")
    else:
        print("No it cannot be")
