def getSum(arr, n):
    temp = []
    x = (n - 1) // 2
    p = pow(2, n) - 1
    temp.append(p)
    y = n - 2
    num = p
    p1=pow(2,n-1)
    p2=1
    for i in range(1, x + 1):
        p1=p1//2
        # p2=p2*2
        num = num + p1-pow(2,i-1)
        # print("num= ",num)
        temp.append(num)

    if n % 2 == 0:
        temp.append(temp[x])

    for a in range(x - 1, -1, -1):
        temp.append(temp[a])

    result = 0
    MOD = 1000000007
    for i in range(n):
        q = temp[i]
        r = arr[i]
        result = result + (q * r)%MOd
        result = result % MOD
    return result


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sum = getSum(arr, n)
    print(sum)
