class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def sortedArrayToBST(arr):
    if(len(arr) is 1):
        return Node(arr[0])
    l=int(len(arr)/2)
    node=Node(arr[l])
    node.left=sortedArrayToBST(arr[0:l])
    node.right=sortedArrayToBST(arr[l+1:])
    return node


def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)


if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = sortedArrayToBST(arr)
    print("PreOrder Traversal of constructed BST ")
    preOrder(root)