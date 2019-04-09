class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if root.data > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def isTripletPresent(root):
    node = convertBSTtoDLL(root)
    head = node
    tail = node
    while (head.left is not None):
        head = head.left
    print("printing the sequenc")

    # while(head is not None):
    #     print(head.data,end=" ")
    #     head=head.right

    while (tail.right is not None):
        tail = tail.right
    # print("head = ",head.data)
    # print("tail = ",tail.data)

    while (head.right is not None and head.data < 0):
        # print("here",head.data)
        if (isPresent(head.right, tail, -(head.data))):
            return True
        else:
            head = head.right
    return False


def isPresent(head, tail, key):
    while (head != tail):
        if (head.data + tail.data == key):
            return True
        if (head.data + tail.data > key):
            tail = tail.left
        else:
            head = head.right


def convertBSTtoDLL(root):
    if root is None:
        return root
    if (root.left is not None):
        left = convertBSTtoDLL(root.left)
        while (left.right is not None):
            left = left.right
        left.right = root
        root.left = left

    if (root.right is not None):
        right = convertBSTtoDLL(root.right)
        while (right.left is not None):
            right = right.left
        right.left = root
        root.right = right
    return root


if __name__ == "__main__":
    root = None
    root = insert(root, 6)
    root = insert(root, -13)
    root = insert(root, 14)
    root = insert(root, -8)
    root = insert(root, 13)
    root = insert(root, 7)

    if (isTripletPresent(root)):
        print("Present")
    else:
        print("Not present")
