def findIndex(dict, value, x):
    print("dict[value]= ", dict[value], " value= ", value)
    if len(dict[value]) == 1:
        return dict[value][0]
    else:
        # for i in range(len(dict[value])):
        #     if dict[value][i] > x:
        #         return dict[value][i]
        x=dict[value][0]
        dict[value].remove(x)
        return x

    # return dict[value]


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def updateDict(dict, i, index, valueI, valueIndex):

    print("dict[valueI]",dict[valueI]," index= ",index)
    print("dict[valueIndex]", dict[valueIndex], " index= ", index)

    # dict[valueI].remove(index)
    # dict[valueIndex].remove(i)
    dict[valueI].append(index)
    dict[valueIndex].append(i)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    arr2 = []
    arr3 = []
    arr4 = []
    dict1 = {}
    dict2 = {}

    for i in range(n):
        if arr[i] in dict1 and arr[i] in dict2:
            dict1[arr[i]].append(i)
            dict2[arr[i]].append(i)

        dict1[arr[i]] = []
        dict1[arr[i]].append(i)
        dict2[arr[i]] = []
        dict2[arr[i]].append(i)
        # dict2[arr[i]] = i
    # print(dict)
    print(dict1)
    print(dict2)

    for i in range(n):
        arr2.append(arr[i])
        arr3.append(arr[i])
        arr4.append(arr[i])

    arr2.sort()
    arr3.sort(reverse=True)
    count1 = 0
    count2 = 0
    # print(arr3)
    for i in range(n):
        if arr4[i] == arr2[i]:
            continue
        else:
            index = findIndex(dict1, arr2[i], i)
            swap(arr4, i, index)
            updateDict(dict1, i, index, arr4[i], arr4[index])
            count1 += 1
    for i in range(n):
        if arr[i] == arr3[i]:
            continue
        else:
            index = findIndex(dict2, arr3[i], i)
            swap(arr, i, index)
            updateDict(dict2, i, index, arr[i], arr[index])
            count2 += 1

    print(min(count1, count2))
