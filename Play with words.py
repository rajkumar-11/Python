def getTheProduct(s):
    length = len(s)
    # print("length= ",length)
    temp = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        temp[i][i] = 1

    for l in range(2, length + 1):
        for i in range(0, length - l + 1):
            j = i + l - 1
            if s[i] == s[j] and j == i + 1:
                temp[i][j] = 2
            elif s[i] == s[j]:
                temp[i][j] = temp[i + 1][j - 1] + 2
            else:
                temp[i][j] = max(temp[i + 1][j], temp[i][j - 1])
    # print(temp)
    product = -9999
    for i in range(0, length):
        left = 0
        right = 0
        left = getMaximum(temp[0][0:i])
        right = getMaximum(temp[i][i:])
        maxValue = left * right
        if (maxValue > product):
            product = maxValue
    return product


def getMaximum(arr):
    l = len(arr)
    max = -99
    for i in range(l):
        if arr[i] > max:
            max = arr[i]
    return max


if __name__ == "__main__":
    s = input()
    result = getTheProduct(s)
    print(result)
