class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if root.val > key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getbalance(root)
        # print("balance= ", balance)

        if (balance > 1 and key < root.left.val):
            return self.rightRotate(root)
        elif (balance < -1 and key > root.right.val):
            return self.leftRotate(root)
        elif (balance > 1 and key > root.left.val):
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif (balance < -1 and key < root.right.val):
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if (root.val < key):
            root.right= self.delete(root.right, key)
        elif (root.val > key):
            root.left=self.delete(root.left, key)
        else:
            if root.left is None:
                temp = root.right
                root=None
                return temp
            elif root.right is None:
                temp = root.left
                root=None
                return temp
            else:
                temp = getMinimum(root.right)
                root.val=temp.val
                root.right=self.delete(root.right,temp.val)

        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))


        balance= self.getbalance(root)

        if balance>1 and self.getbalance(root.left)>=0:
            return self.rightRotate(root)
        if balance<-1 and self.getbalance(root.right)<=0:
            return self.leftRotate(root)
        if balance >1 and self.getbalance(root.left)<0:
            root.left=self.leftRotate(root.left)
            return elf.rightRotate(root)
        if balance<-1 and self.getbalance(root.right)<0:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        # if (balance > 1 and key < root.left.val):
        #     return self.rightRotate(root)
        # elif (balance < -1 and key > root.right.val):
        #     return self.leftRotate(root)
        # elif (balance > 1 and key > root.left.val):
        #     root.left = self.leftRotate(root.left)
        #     return self.rightRotate(root)
        # elif (balance < -1 and key < root.right.val):
        #     root.right = self.rightRotate(root.right)
        #     return self.leftRotate(root)



        return root




    def getMininmum(self, root):
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        return self.getMininmum(root.left)

    def getbalance(self, root):
        if root is None:
            return 0
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return root.height;

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # assinging
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T2 = y.right

        # Assigning
        y.right = z
        z.left = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def preOrder(self, root):
        if root is None:
            return
        print(root.val, end="  ")
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    myTree = AVLTree()
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    root = None

    for num in nums:
        print("num= ", num)
        root = myTree.insert(root, num)

    """The constructed AVL Tree would be 
                30 
               /  \ 
             20   40 
            /  \     \ 
           10  25    50"""

    print("Preorder traversal of the",
          "constructed AVL tree is")
    myTree.preOrder(root)
    print()
    key = 10
    root = myTree.delete(root, key)
    print("Preorder Traversal after deletion -")
    myTree.preOrder(root)
    print()
