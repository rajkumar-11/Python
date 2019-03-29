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
        print("balance= ", balance)

        if (balance > 1 and key < root.left.val):
            return self.rightRotate(root)
        elif (balance < -1 and key > root.right.val):
            return self.leftRotate(root)
        elif (balance > 1 and key > root.left.val):
            root.left = self.leftRotate(root.left)
            self.rightRotate(root)
        elif (balance < -1 and key < root.right.val):
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

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

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        return y

    def preOrder(self, root):
        if root is None:
            return
        print(root.val, end="  ")
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    myTree = AVLTree()
    root = None

    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

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
