def findAndSum(arr, n):
    sum = 0
    mul = 1
    flag = False
    count = 0

    for i in range(0, 30):
        count = 0
        for j in range(n):
            if True if (arr[j] & (1 << i)) >0 else False:
                if (flag is True):
                    count = count + 1
                else:
                    flag = True
                    count += 1
            elif flag is True:
                # print("here")
                print("count= ", count)
                sum += (mul * count * (count + 1) // 2)
                flag = False
                count = 0
        if flag is True:
            sum += ((mul * count * (count + 1)) // 2)
        mul = mul * 2
    return sum


if __name__ == "__main__":
    arr = [7, 1, 1, 5,11,21,23]
    n = len(arr)
    print(findAndSum(arr, n))
