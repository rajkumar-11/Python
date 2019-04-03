class Node:
    def __init__(self,char):
        self.char=char
        self.right=None
        self.left=None

# preindex=0


class BuildTree:
    def __init__(self):
        self.preindex=0

    def buildTree(self,inorder,preOrder,start,end):
        # print("start= ",start," end= ",end," preindex= ",self.preindex)
        if start>end:
            return None

        node = Node(preOrder[self.preindex])
        self.preindex = self.preindex + 1
        if start== end:
            return node


        # self.preindex=self.preindex+1
        index=inorder.index(preOrder[self.preindex-1])
        # print("index= ",index)
        node.left=self.buildTree(inorder,preOrder,start,index-1)
        # self.preindex = self.preindex + 1
        node.right=self.buildTree(inorder,preOrder,index+1,end)
        return node


    def printInorder(self,root):
        if root is None:
            return
        self.printInorder(root.left)
        print(root.char,end=" ")
        self.printInorder(root.right)





if __name__=="__main__":
    inOrder = ['D', 'B', 'E', 'A', 'A', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'A']
    tree=BuildTree()

    preIndex = 0
    root = tree.buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
    # print(root.char)
    # Let us test the build tree by priting Inorder traversal
    print("Inorder traversal of the constructed tree is")
    tree.printInorder(root)