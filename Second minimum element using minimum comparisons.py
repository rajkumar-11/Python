class Node:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None


def findSecondMin(arr, n):
    list = []
    for i in range(0, n, 2):
        t1 = Node(i)
        t2 = None
        if (i + 1 < n):
            t2 = Node(i + 1)
            root = Node(i) if arr[i] < arr[i + 1] else Node(i + 1)
            root.left = t1
            root.right = t2
            list.append(root)
        else:
            list.append(t1)

    lsize = len(list)

    while (lsize != 1):
        last = lsize - 2 if lsize & 1 else lsize - 1
        for i in range(0, last, 2):
            f1 = list.pop()
            f2 = list.pop()
            root = Node(f1.index) if arr[f1.index] < arr[f2.index] else Node(f2.index)
            root.left = f1
            root.right = f2
            list.append(root)
        if (lsize & 1):
            node = list.pop()
            list.append(node)
        lsize = len(list)

    res = 9999999999999
    res = traverseHeight(root, arr, res)
    # print("res final= ", res)
    print("Minimun = ", arr[root.index], " second minimum = ", res)


def traverseHeight(root, arr, res):
    # print("res= ", res)
    if root is None or (root.left is None and root.right is None):
        return res

    if (res > arr[root.left.index] and root.left.index is not root.index):
        res = arr[root.left.index]
        # print("res= ",res)
        return traverseHeight(root.right, arr, res)
    elif (res > arr[root.right.index] and root.right.index is not root.index):
        res = arr[root.right.index]
        # print("res= ", res)
        return traverseHeight(root.left, arr, res)
    return res


if __name__ == "__main__":
    arr = [61, 6, 100, 9,10,12, 17]
    n = len(arr)
    findSecondMin(arr, n)
