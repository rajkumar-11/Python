def findMax(n, B):
    maxi = 0
    max1 = 0
    for i in range(1, n):
        prev = B[i - 1]
        curr = B[i]
        newMaxi = max(maxi + abs(prev - curr), max1 + (curr - 1))
        newMax1 = max(maxi + abs(1 - prev), max1 + (curr - 1))
        maxi, max1 = newMaxi, newMax1
    return max(max1, maxi)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        B = list(map(int, input().split()))
        maxr = findMax(n, B)
        print(maxr)
