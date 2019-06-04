def findIndex(dict, value):
    return dict[value]


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def updateDict(dict, i, index, valueI, valueIndex):
    dict[valueI] = i
    dict[valueIndex] = index


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    arr2 = []
    arr3 = []
    arr4 = []
    dict1 = {}
    dict2 = {}

    for i in range(n):
        dict1[arr[i]] = i
        dict2[arr[i]] = i
    # print(dict)

    for i in range(n):
        arr2.append(arr[i])
        arr3.append(arr[i])
        arr4.append(arr[i])

    arr2.sort()
    arr3.sort(reverse=True)
    count1 = 0
    count2 = 0
    for i in range(n - 1):
        if arr4[i] == arr2[i]:
            continue
        else:
            index = findIndex(dict1, arr2[i])
            # print(arr4)
            swap(arr4, i, index)
            # print(arr4)
            updateDict(dict1, i, index, arr4[i], arr4[index])
            count1 += 1
    for i in range(n - 1):
        if arr[i] == arr3[i]:
            continue
        else:
            index = findIndex(dict2, arr3[i])
            swap(arr, i, index)
            # updateDict(dict2,i,index,)
            dict2[arr[i]] = i
            dict2[arr[index]] = index
            count2 += 1

    print(min(count1, count2))
