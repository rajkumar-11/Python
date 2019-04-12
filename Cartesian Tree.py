class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


def buildCartesianTree(arr, n):
    parent = [-1] * n
    left = [-1] * n
    right = [-1] * n

    root = 0
    last = None
    for i in range(1, n):
        last = i - 1
        right[i] = -1
        while (arr[last] <= arr[i] and last != root):
            last = parent[last]

        if (arr[last] <= arr[i]):
            parent[root] = i
            left[i] = root
            root = i
        elif right[last] == -1:
            right[last] = i
            parent[i] = last
            left[i] = -1
        else:
            parent[right[last]] = i
            left[i] = right[last]
            right[last] = i
            parent[i] = last

    parent[root] = -1
    return (buildCartesianTreeUtil(root, arr, parent, left, right))


def buildCartesianTreeUtil(root, arr, parent, left, right):
    if root == -1:
        return None
    node = Node(arr[root])
    node.left = buildCartesianTreeUtil(left[root], arr, parent, left, right)
    node.right = buildCartesianTreeUtil(right[root], arr, parent, left, right)
    return node


if __name__ == '__main__':
    # Assume that inorder traversal of
    # following tree is given
    #    40
    # / \
    # 10     30
    # /      \
    # 5       28

    inorder = [5, 10, 40, 30, 28]
    Len = len(inorder)
    root = buildCartesianTree(inorder, Len)

    # Let us test the built tree by
    # printing Insorder traversal
    print("Inorder traversal of the",
          "constructed tree is ")
    printInorder(root)
