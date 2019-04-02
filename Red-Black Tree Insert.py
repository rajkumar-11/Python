import enum

class Color(enum.Enum):
    black=0
    red=1

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

    def insert(self,root,data):
        # node=RBNode(data)
        if root is None:
            return RBNode(data)
        if(root.data>data):
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)




        return root











if __name__=="__main__":
    tree=RBTree()
    root=tree.insert(root,7)

    root=tree.insert(root,6)
    root=tree.insert(root,5)
    root=tree.insert(root,4)
    root=tree.insert(root,3)
    root=tree.insert(root,2)
    root=tree.insert(root,1)
    print("InOrder Traversal of Created Tree")
    tree.inOrder()
    print("Leve Order Traversal of created Tree")
    tree.levelOrder()

