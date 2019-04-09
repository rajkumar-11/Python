class Interval:
    def __init__(self,low,high  ):
        self.low = low
        self.high = high


class Node:
    def __init__(self, i):
        self.Interval = i
        self.max = i.high
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print("[ ", root.Interval.low, ",", root.Interval.high, " ]", " max= ", root.max)
    inorder(root.right)


def overlapSearch(root, x):
    if root is None:
        return None

    if (isOverlapping(root.Interval, x)):
        return root.Interval

    if (root.left is not None and root.left.max >= x.low):
        return overlapSearch(root.left, x)

    return overlapSearch(root.right, x)


def isOverlapping(I1, I2):
    if (I1.low <= I2.low and I1.high >= I2.high):
        return True
    return False


def insert(root, x):
    if root is None:
        return Node(x)
    l = root.Interval.low
    if (l > x.low):
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)

    if (root.max < x.high):
        root.max = x.high
    return root


if __name__ == "__main__":
    ints = [Interval(15, 20),Interval(10, 30), Interval(17, 19), Interval(5, 20), Interval(12, 15), Interval(30, 40)]
    print(len(ints))

    root=None

    for i in range(len(ints)):
        root = insert(root, ints[i])

    print("InORder Traversal of constructed Interval Trees is \n")
    inorder(root)
    x = Interval(6, 7)
    print("searching for Interval [", x.low, ",", x.high, "]")
    res = overlapSearch(root, x)
    if res is None:
        print("No Overlapping Interval")
    else:
        print("Overlap with [", res.low, " ", res.high, "]")
