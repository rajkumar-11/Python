class BTreeNode:
    def __init__(self,t):
        self.t

    def splitChild(self,i,y):
        z=BTreeNode(y.t,y.leaf)
        z.n=t-1
        for j in range(t-1):
            z.keys[i]=y.keys[j+t]
        if(y.leaf is False):
            for j in range(t):
                z.C[j]=y.C[j+t]

        y.n=t-1
        for(j=n)





class BTree:
    def __init__(self, t):
        self.root=None
        self.t=t
    def traverst(self):





    def insert(self,k):
        if(self.root is None):
            self.root=BTreeNode(self.t,True)
            self.root.keys[0]=k
            self.root.n=1
        else:
            if(self.root.n=2*self.t-1):
                s=BTreeNode(t,False)
                s.C[0]=self.root
                s.splitChild(0,self.root)























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