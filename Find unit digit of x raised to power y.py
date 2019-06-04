from math import sqrt


def canBeExpressedAsPower(n):
    x = int(sqrt(n))
    # print("x= ",x)
    for i in range(2, x + 1):
        p = i
        while (p <= n):
            if p == n:
                return True
            p = p * i
    return False


if __name__ == "__main__":
    n = int(input())
    if (canBeExpressedAsPower(n)):
        print("Yes it can be")
    else:
        print("No it cannot be")
