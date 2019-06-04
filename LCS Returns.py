def getCount(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp1 = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp1[i][j] = dp1[i - 1][j - 1] + 1
            else:
                dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1])

    # print(dp1)
    lcs = dp1[l1][l2] + 1

    s11 = s1[::-1]
    s22 = s2[::-1]
    l1 = len(s11)
    l2 = len(s22)

    dp2 = [[0 for i in range(l2 + 1)] for i in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s11[i - 1] == s22[j - 1]:
                dp2[i][j] = dp2[i - 1][j - 1] + 1
            else:
                dp2[i][j] = max(dp2[i - 1][j], dp2[i][j - 1])

    # print(dp2)
    ans = 0

    # for j in range(0,l2):
    #     for i in range(0,l1):
    #         print("c= ",dp1[i][j-1]+1+dp2[l1-i][l2-j-1])
    #         if (dp1[i+1][j-1]+1+dp2[l1-i][l2-j-1]==lcs):
    #             ans=ans+1

    sets = set()
    for i in range(len(s2)):
        sets.add(s2[i])
    list1 = list(sets)
    # list1.sort()
    # print("list1=", list1)
    # print("s2= ",s2)
    # print("lcs= ",lcs)
    list2 = [[] for j in range(1000)]
    findAlloccurances(s2, list2)
    # print(list2)

    for i in range(l1 + 1):
        for j in range(len(list1)):
            for k in range(len(list2[ord(list1[j])])):
                x = list2[ord(list1[j])][k]
                if (dp1[i][x] + 1 + dp2[l1 - i][l2 - x-1]) == lcs:
                    ans += 1
                    break

    return ans


def findAlloccurances(s2, list2):
    length = len(s2)
    for i in range(length):
        list2[ord(s2[i])].append(i)


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    count = getCount(s1, s2)
    print(count)
