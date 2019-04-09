import enum

class Color(enum.Enum):
    Black=0
    Red=1

class RBNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        self.color=None





class RBTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        node=RBNode(data)
        self.root=self.insertNode(self.root,node)
        self.fixViolations(self.root,node)

    def fixViolations(self,root,node):
        parent=None
        grandParent=None
        while(node is not root and node.color is not Black and node.parent.color is Red):
            parent=node.parent
            grandParent=node.parent.parent

            if (parent is grandParent.left):
                uncle=grandParent.right
                if uncle is not None and uncle.color is Red:
                    grandParent.color=Red
                    parent.color=Red
                    uncle.color=Red
                    node=grandParent
                else:
                    if(node==parent.right):
                        self.rotateLeft(root,parent)
                        node=parent
                        parent=node.parent
                    rotateRight(root,grandParent)
                    self.swap(parent.color,grandParent.color)
                    node=parent
            else:
                uncle=grandParent.left
                if(uncle is not None and uncle.color is red):
                    grandParent.color=Red
                    parent.color=Black
                    uncle.color=Black
                    node=grandParent
                else:
                    if(node is parent.left):
                        self.rotateRight(root,grandParent)
                        node=parent
                        parent=node.parent
                    self.rotateLeft(root,grandParent)
                    swap(parent.color,grandparent.color)
                    node=parent
        root.color=Black


    def rotateLeft(self,root,node):







    def insertNode(self,root,node):
        if root is None:
            return node
        if root.data>node.data:
            root.left=self.insertNode(root.left,node)
            root.left.parent=root
        else:
            root.right=self.insertNode(root.right,node)
            root.right.parent=root
        return root;











if __name__=="__main__":
    tree=RBTree()
    tree.insert(7)
    tree.insert(6)
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    print("InOrder Traversal of Created Tree")
    tree.inOrder()
    print("Leve Order Traversal of created Tree")
    tree.levelOrder()

