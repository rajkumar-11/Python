class NodeTrie:
    def __init__(self):
        # self.char=char
        self.count=0
        self.child=[]
        for i in range(26):
            self.child.append(None)


class Trie:
    def __init__(self):
        self.root=NodeTrie()


def add(string,root,index,len):
    # if index>=len:
    #     return

    # if root.child[ord(string[index]) - 97] is None:
    #     root.child[ord(string[index]) - 97]= NodeTrie()
    # root.child[ord(string[index]) - 97].count+=1
    # add(string,root.child[ord(string[index]) - 97],index+1,len)
    for i in range(len):
        if root.child[ord(string[i]) - 97] is None:
            root.child[ord(string[i]) - 97]=NodeTrie()
            root= root.child[ord(string[i]) - 97]
        else:
            root = root.child[ord(string[i]) - 97]
        root.count=root.count+1


def find(string,root,index,len):
    if index==len:
        if (root  is not None):
            print(root.count)
        else:
            print(0)
        return
    if root.child[ord(string[index]) - 97] is None:
        print(0)
        return
    else:
        find(string,root.child[ord(string[index]) - 97],index+1,len)


if __name__=="__main__":
    x=int(input())
    trie=Trie()
    for i in range(x):
        op,string=input().split()
        # print("op =",op," string= ",string)
        if op=="add":
            # print("here")
            add(string,trie.root,0,len(string))
        if op=="find":
            find(string,trie.root,0,len(string))





