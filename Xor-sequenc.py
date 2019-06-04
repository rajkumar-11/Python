def getValue(arr, r, max):
    # print("here")

    if r < max:
        return arr[r]
    else:
        value = arr[max - 1]
        for i in range(max, r):
            value = value ^ i
        return value


def xorValue(r, s):
    value = 0
    for i in range(r, s + 1, 2):
        # print("i= ",i)
        value = value ^ i
    return value


if __name__ == "__main__":
    q = int(input())
    arr = [None for i in range(10000000)]
    arr[0] = 0
    max = 10000000
    for i in range(1, 10000000):
        arr[i] = arr[i - 1] ^ i

    for i in range(q):
        l = list(map(int, input().split()))
        r = l[0]
        s = l[1]
        diff = (s - r + 1)
        if diff % 2 == 0:
            value = xorValue(r + 1, s)
            print(value)
        else:
            # print("here1")
            value = getValue(arr, r-1, max) ^ xorValue(r, s)
            print(value)

        # value=getValue(r)

        # print(value)
