class Unique:

    def __init__(self):
        M = [[0, 1, 0],
             [1, 0, 1,],
             [0, 1, 1],
             [1, 1, 1],
             [0,1,0],
             [1,0,1],
             [0,0,0]
             ];
        self.findUniqueRows(M);


    def findUniqueRows(self,M):
        length = len(M)
        # print("length= ", length)
        Row = len(M[0])
        # print("Row= ", Row)
        trie = Trie()
        for i in range(length):
            # print("hello")
            trie.insert(M[i]);
        x=[]
        # x.append()
        trie.NumberOfUniqueRows(trie.root,x)
        # print("count= ",count)


class Trie:
    root = None
    # def __init__(self):
    #     # self.a = a
    #     self.child=ch
    #     self.child[0] = None
    #     self.child[1] = None

    def insert(self, arr):
        if self.root is None:
            self.root = NodeTrie();
        node = self.root
        for i in range(len(arr)):
            if node.child[arr[i]] is None:
                # print("jjkk")
                if i==len(arr)-1:
                    node.child[arr[i]] = NodeTrie()
                    node.child[arr[i]].isEndOfCol=True
                else:
                    node.child[arr[i]] = NodeTrie()
                    node=node.child[arr[i]]
            else:
                node=node.child[arr[i]]



    def NumberOfUniqueRows(self,root,x):
        if root is None:
            return
        # print("xyz")

        if root.isEndOfCol==True:
            # count+=1;
            # print("jai shree ram")
            print(x)
        x.append('0')
        self.NumberOfUniqueRows(root.child[0],x)
        x.pop()
        x.append('1')
        self.NumberOfUniqueRows(root.child[1],x)
        x.pop()


class NodeTrie:
    def __init__(self):
        self.isEndOfCol=False
        self.child=[];
        self.child.append(None)
        self.child.append(None)



if __name__=="__main__":
    unique=Unique()
