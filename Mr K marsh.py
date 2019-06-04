def getValue(x1, y1, x2, y2):
    # print("x1= ", x1, "y1= ", y1, " x2 = ", x2, " y2= ", y2)
    return 2 * (x2 - x1) + 2 * (y2 - y1)


if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    arr = [None for i in range(m)]
    for i in range(m):
        arr[i] = input()
    # print(arr)
    left = [[0 for i in range(n)] for j in range(m)]
    top = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                if arr[i][j] == '.':
                    top[i][j] = 0
                else:
                    top[i][j] = -1
            else:
                if arr[i][j] == '.':
                    top[i][j] = top[i - 1][j] + 1
                else:
                    top[i][j] = -1

    for j in range(n):
        for i in range(m):
            if j == 0:
                if arr[i][j] == '.':
                    left[i][j] = 0
                else:
                    left[i][j] = -1
            else:
                if arr[i][j] == '.':
                    left[i][j] = left[i][j - 1] + 1
                else:
                    left[i][j] = -1
    # # print("Left")
    # for i in range(m):
    #     for j in range(n):
    #         print(left[i][j], end=" ")
    #     print()
    #
    # print()
    # # print("top")
    # for i in range(m):
    #     for j in range(n):
    #         print(top[i][j], end=" ")
    #     print()
    # print()

    max = -1

    # for i in range(m):
    #     for j in range(n):
    # i = 3
    # j = 4

    # print("leftIndex", leftIndex)
    # print("topIndex", topIndex)
    for i in range(m):
        for j in range(n):
            leftIndex = left[i][j]
            topIndex = top[i][j]
            if leftIndex == -1 or topIndex == -1:
                # print("abc")
                continue
            for x in range(1, leftIndex + 1):
                for y in range(1, topIndex + 1):
                    lefttop = top[i][j - x]
                    topleft = left[i - y][j]
                    x1 = j - x
                    y1 = i - lefttop
                    x2 = j - topleft
                    y2 = i - y
                    # print("x1= ",x1,"y1= ",y1," x2 = ",x2," y2= ",y2)
                    if x1 == x2 and y1 == y2:
                        value = getValue(x1, y1, i, j)
                        if value > max:
                            max = value

    if max==-1:
        print("impossible")
    else:
        print(max)
