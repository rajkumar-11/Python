class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class TreeToBST:
    head=None
    prev=None
    def BinaryTree2DoubleLinkedList(self,root):
        if root is None:
            return root
        self.BinaryTree2DoubleLinkedList(root.left)
        if(self.prev is None):
            self.head=root
        else:
            root.left=self.prev
            self.prev.right=root
        self.prev = root
        self.BinaryTree2DoubleLinkedList(root.right)

def printDLL(head):
    while head is not None:
        print(head.data,end=" ")
        head=head.right


if __name__=="__main__":
    root=Node(10)
    root.left=Node(12)
    root.right=Node(15)
    root.left.left=Node(25)
    root.left.right=Node(30)
    root.right.left=Node(36)
    conversion=TreeToBST()
    conversion.BinaryTree2DoubleLinkedList(root)
    printDLL(conversion.head)

