from openpyxl.descriptors import String


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.char = key


def isSubTree(T, S):
    preOrderT = []
    inOrderT = []
    preOrderS = []
    inOrderS = []

    preOrder(T, preOrderT)
    inOrder(T, inOrderT)
    # print("root s ",S.char)

    preOrder(S, preOrderS)
    inOrder(S, inOrderS)
    print(preOrderT)
    print(inOrderT)
    print(preOrderS)
    print(inOrderS)
    preOrderT = ''.join(preOrderT)
    preOrderS = ''.join(preOrderS)
    inOrderS = ''.join(inOrderS)
    inOrderT = ''.join(inOrderT)

    if (preOrderS in preOrderT and inOrderS in inOrderT):
        return True
    return False


def preOrder(root, string):
    if root is None:
        return
    string.append(root.char)
    preOrder(root.left, string)
    preOrder(root.right, string)


def inOrder(root, string):
    if root is None:
        return
    inOrder(root.left, string)
    string.append(root.char)
    inOrder(root.right, string)


if __name__ == "__main__":
    T = Node('z')
    T.left = Node('x')
    T.right = Node('e')
    T.left.left = Node('a')
    T.left.right = Node('b')
    T.left.left.right = Node('c')
    T.right.right = Node('k')

    S = Node('x')
    S.left = Node('a')
    S.left.right = Node('c')
    S.right = Node('b')

    if (isSubTree(T, S) is True):
        print("Yes: S is subtree of T")
    else:
        print("No: S is not subtree of T")
