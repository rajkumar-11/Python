def getCount(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    # print("sum= ", sum)
    if sum==0:
        return n-1
    else:
        return getSumUtils(arr, 0, n - 1, sum)


def getSumUtils(arr, start, end, sum):
    # print("sum here ",sum," start= ",start," end= ",end)
    if sum % 2 != 0:
        return 0
    # print("xsds")

    if end <= start:
        return 0

    tempsum = 0
    index = -1
    flag = False
    # print("jais h")
    for i in range(start, end):
        tempsum = tempsum + arr[i]
        # print("tempsum= ",tempsum)
        if tempsum == sum//2:
            index = i
            flag = True
            break
    if flag == False:
        return 0
    else:
        return max(1 + getSumUtils(arr, start, index, sum // 2), 1 + getSumUtils(arr, index + 1, end, sum // 2))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        count = getCount(arr, n)
        print(count)
