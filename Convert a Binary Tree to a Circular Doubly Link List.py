from numpy.ma import left_shift


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bTreeToCList(root):
    if root is None:
        return root
    left = bTreeToCList(root.left)
    right = bTreeToCList(root.right)
    root.left = root.right = root
    return concatenate(concatenate(left, root), right)


def concatenate(leftSide, rightSide):
    if(leftSide is None):
        return rightSide
    if(rightSide is None):
        return leftSide
    leftlast = leftSide.left
    rightlast = rightSide.left

    leftlast.right = rightSide
    rightSide.left = leftlast
    leftSide.left = rightlast
    rightlast.right = leftSide

    return leftSide


def display(head):
    itr = head
    first=True
    while (itr!=head  or first ):
        print(itr.data, end=" ")
        itr=itr.right
        first=False


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    head = bTreeToCList(root)
    display(head)
