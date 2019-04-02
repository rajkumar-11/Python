clastt BTreeNode:


class BTree:
    def __init__(self, t):
        self.root=None
        self.t=t
    def traverst(self):




















if __name__=="__main__":
    t=BTree(3)
    t.insert(10)
    t.insert(20)
    t.insert(5)
    t.insert(6)
    t.insert(12)
    t.insert(30)
    t.insert(7)
    t.insert(17)
    print("Traversal of constructed tree is ")
    t.traverse()