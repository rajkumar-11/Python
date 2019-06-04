def FindAllThePrimesLessThan(n):
    arr = [True] * (n)
    arr[0] = False
    arr[1] = False

    p = 2
    while (p * p < n):
        if arr[p] is True:
            i = p * p
            while (i < n):
                arr[i] = False
                i = i + p
        p = p + 1

    return arr


if __name__ == "__main__":
    q = int(input())
    primeArr = FindAllThePrimesLessThan(8192)
    for i in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        # x = 8191
        sets = set()
        temp = [0] * 8192
        # temp[0] = 1
        for i in range(n):
            sets.add(arr[i])

        li = list(sets)
        print(li)
        for a in range(len(arr)):
            temp[arr[a]] = 1

        for j in range(len(arr)):
            for k in range(0, 8192):
                if temp[k] > 0:
                    temp[k ^ arr[j]] += 1
                    print("value= ", k ^ arr[j], " k= ", k)
        count = 0

        # print(temp)
        print(li)

        for i in range(2, 8192):
            if primeArr[i] is True and temp[i] > 0:
                print("i= ", i, " count = ", temp[i])
                count += temp[i]

        print(count % 1000000007)

    # temp[]
