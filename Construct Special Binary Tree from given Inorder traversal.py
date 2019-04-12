class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def buildTree(inorder, start, end):
    if (start > end):
        return None
    # print("start =",start," end= ",end)
    index = findMaxIndex(inorder, start, end)
    root = Node(inorder[index])

    if start == end:
        return root
    root.left = buildTree(inorder, start, index - 1)
    root.right = buildTree(inorder, index + 1, end)
    return root


def findMaxIndex(inorder, start, end):
    index = start
    max = inorder[start]
    for i in range(start+1, end + 1):
        if inorder[i] > max:
            max = inorder[i]
            index = i
    return index


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


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
    root = buildTree(inorder, 0, Len - 1)

    # Let us test the built tree by
    # printing Insorder traversal
    print("Inorder traversal of the",
          "constructed tree is ")
    printInorder(root)
