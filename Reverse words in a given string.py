def reverse(string):
    l = len(string)
    reverse = []
    for i in range(l):
        reverse.append(string[l - 1 - i])
    # reverseString=''.join(reverse)
    print(reverse)

    i = 0
    while (i < l):
        j = i
        if (reverse[j] is ' '):
            i = i + 1
            continue

        while (j <= l - 1 and reverse[j] is not ' '):
            j = j + 1
        swap(reverse, i, j - 1)
        i = j
    return ''.join(reverse)


def swap(string, i, j):
    print("i =", i, " j= ", j)
    while (i < j):
        temp = string[i]
        string[i] = string[j]
        string[j] = temp
        i = i + 1
        j = j - 1


if __name__ == "__main__":
    string = "i like this program very much"
    print(reverse(string))
