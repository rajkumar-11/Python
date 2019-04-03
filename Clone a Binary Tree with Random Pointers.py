class RandomNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.random=None

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print("[",root.key,",",end="")
    if root.random is None:
        print("NULL"," ]",end=" ")
    else:
        print(root.random.key," ]",end=" ")
    printInorder(root.right)

def cloneTree(root,i,visited,dict):
    if root is None:
        return root
    if visited[i] is True:
        return dict.get(root)
    visited[i]=True

    rootc=RandomNode(root.key)
    dict[root]=rootc
    rootc.left=cloneTree(root.left,2*i+1,visited,dict)
    rootc.right=cloneTree(root.right,2*i+2,visited,dict)
    rootc.random=cloneTree(root.random,-1,visited,dict)
    return rootc


def getHeight(root):
    if root is None:
        return 0;
    else:
        return 1+max(getHeight(root.left),getHeight(root.right))



if __name__=="__main__":
    # print("here")
    # tree=RandomNode(1)
    # tree.left=RandomNode(2)
    # tree.right=RandomNode(3)
    # tree.left.left=RandomNode(4)
    # tree.left.right = RandomNode(5)
    # tree.random=tree.left.right
    # tree.left.left.random=tree
    # tree.left.right.random=tree.right
    tree = RandomNode(10);
    n2 = RandomNode(6);
    n3 = RandomNode(12);
    n4 = RandomNode(5);
    n5 = RandomNode(8);
    n6 = RandomNode(11);
    n7 = RandomNode(13);
    n8 = RandomNode(7);
    n9 = RandomNode(9);
    tree.left = n2;
    tree.right = n3;
    tree.random = n2;
    n2.left = n4;
    n2.right = n5;
    n2.random = n8;
    n3.left = n6;
    n3.right = n7;
    n3.random = n5;
    n4.random = n9;
    n5.left = n8;
    n5.right = n9;
    n5.random = tree;
    n6.random = n9;
    n9.random = n8;

    print("InOrder traversal of original tree")
    printInorder(tree)

    h = getHeight(tree)
    n = pow(h, 2) - 1
    visited = [False] * n
    print()
    dict={}
    clone=cloneTree(tree,0,visited,dict)
    print("InOrder traversal of clone trees is")
    printInorder(clone)


    tree.key=1
    n2.key=2
    n3.key=3
    n4.key=4
    n5.key=5
    n6.key=6
    n7.key=7
    n8.key=8
    n9.key=9
    print()
    print("InOrder traversal of original tree after modification is ")
    printInorder(tree)
    print()
    print("InOrder traversal of clone trees is")
    printInorder(clone)

