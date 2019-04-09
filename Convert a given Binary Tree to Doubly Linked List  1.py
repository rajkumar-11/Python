class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class TreeToBST:

    def BinaryTree2DoubleLinkedList(self,root):
        if root is None:
            return root
        if(root.left is not None):
            left=self.BinaryTree2DoubleLinkedList(root.left)
            while(left.right is not None):
                left=left.right
            left.right=root
            root.left=left

        if root.right is not None:
            right=self.BinaryTree2DoubleLinkedList(root.right)
            while(right.left is not None):
                right=right.left
            right.left=root
            root.right=right
        return root


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
    head=conversion.BinaryTree2DoubleLinkedList(root)
    while(head.left is not None):
        head=head.left
    printDLL(head)

