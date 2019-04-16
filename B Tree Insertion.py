class BTreeNode:
    def __init__(self, t, leaf):
        print("here")
        self.t = t
        self.leaf = leaf
        self.keys = [0] * (2 * t - 1)
        self.C = []
        self.n = 0
    def createChild(self):
        for i in range(2*self.t):
            self.C.append(BTreeNode(self.t,self.leaf))

    def splitChild(self, i, y):
        z = BTreeNode(y.t, y.leaf)
        z.createChild()
        z.n = self.t - 1
        for j in range(self.t - 1):
            z.keys[j] = y.keys[j + self.t]
        if y.leaf == False:
            for j in range(t):
                z.C[j] = y.C[j + self.t]

        y.n = self.t - 1
        for j in range(n, i + 1, -1):
            self.C[j + 1] = self.C[j]
        self.C[i + 1] = z
        for j in range(n - 1, i, -1):
            self.keys[j + 1] = self.keys[j]
        self.keys[i] = y.keys[y.t - 1]
        self.n = self.n + 1

    def insertNonFull(self, k):
        i = self.n - 1
        print("i= ", i, " k= ", k)
        if self.leaf == False:
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i = i - 1
            self.keys[i + 1] = k
            self.n = self.n + 1
        else:
            while (i >= 0 and self.keys[i] > k):
                i = i - 1



            if (self.C[i + 1].n == 2 * self.t - 1):
                print("here")
                self.C[i + 1].splitChild(i + 1, self.C[i + 1])

                if (self.keys[i + 1] < k):
                    i=i+1
            self.C[i + 1].insertNonFull(k)


class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def traverst(self):
        print("x")

    def insert(self, k):
        if (self.root is None):
            self.root = BTreeNode(self.t, True)
            self.root.createChild()
            self.root.keys[0] = k
            self.root.n = 1
        else:
            if (self.root.n == 2 * self.t - 1):
                s = BTreeNode(t, False)
                s.createChild()
                s.C[0] = self.root
                s.splitChild(0, self.root)
                i = 0
                if s.keys[0] < k:
                    i = i + 1
                s.C[i].insertNonFull(k)
                self.root = s
            else:
                self.root.insertNonFull(k)


if __name__ == "__main__":
    t = BTree(3)
    t.insert(10)
    t.insert(20)
    t.insert(5)
    t.insert(6)
    t.insert(12)
    t.insert(30)
    t.insert(7)
    t.insert(17)
    # print("Traversal of constructed tree is ")
    # t.traverse()
