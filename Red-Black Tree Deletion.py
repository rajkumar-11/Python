import enum


class Color(enum.Enum):
    Black = 0
    Red = 1


class RBNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = Color.Red


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = RBNode(data)
        self.root = self.insertNode(self.root, node)
        self.fixViolations(self.root, node)

    def fixViolations(self, root, node):
        parent = None
        grandParent = None

        while (node != root and node.color != Color.Black and node.parent.color == Color.Red):
            parent = node.parent
            grandParent = node.parent.parent

            if (parent is grandParent.left):
                uncle = grandParent.right
                if uncle is not None and uncle.color is Color.Red:
                    grandParent.color = Color.Red
                    parent.color = Color.Black
                    uncle.color = Color.Black
                    node = grandParent
                else:
                    if (node == parent.right):
                        self.rotateLeft(parent)  # here
                        node = parent
                        parent = node.parent
                    self.rotateRight(grandParent)  # there
                    self.swap(parent, grandParent)
                    node = parent
            else:
                uncle = grandParent.left
                if (uncle is not None and uncle.color is Color.Red):
                    grandParent.color = Color.Red
                    parent.color = Color.Black
                    uncle.color = Color.Black
                    node = grandParent
                else:
                    if (node == parent.left):
                        self.rotateRight(parent)
                        node = parent
                        parent = node.parent
                    self.rotateLeft(grandParent)
                    self.swap(parent, grandParent)
                    node = parent
        self.root.color = Color.Black

    def swap(self, parent, grandparent):
        temp = parent.color
        parent.color = grandparent.color
        grandparent.color = temp

    def rotateLeft(self, node):
        right = node.right
        node.right = right.left
        if node.right is not None:
            node.right.parent = node

        right.parent = node.parent

        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def rotateRight(self, node):
        left = node.left
        node.left = left.right
        if node.left is not None:
            node.left.parent = node

        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.left:
            node.parent.left = left
        else:
            node.parent.right = left

        left.right = node
        node.parent = left

    def insertNode(self, rootTemp, node):
        if rootTemp is None:
            return node
        if rootTemp.data > node.data:
            rootTemp.left = self.insertNode(rootTemp.left, node)
            rootTemp.left.parent = rootTemp
        elif rootTemp.data < node.data:
            rootTemp.right = self.insertNode(rootTemp.right, node)
            rootTemp.right.parent = rootTemp
        return rootTemp;

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def levelOrder(self, root):
        queue = []
        queue.append(root)
        while len(queue) is not 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def deleteByVal(self, n):
        if self.root is None:
            return
        v = self.search(n)
        if v.data is not n:
            print("No  node found to delete with value ", n)
            return

        self.deleteNode(v)

    def search(self, n):
        temp = self.root
        while (temp is not None):
            if (n < temp.data):
                if temp.left is None:
                    break
                else:
                    temp = temp.left
            elif (n == temp.data):
                break
            else:
                if temp.right is None:
                    break
                else:
                    temp = temp.right
        return temp

    def deleteNode(self, v):
        u = self.BSTreplace(v)
        uvBlack = True if (u is None or u.color is Color.Black) and (v.color is Color.Black) else False
        parent = v.parent

        if u is None:
            if v is self.root:
                self.root = None
            else:
                if uvBlack:
                    self.fixDoubleBlack(v)
                else:
                    if v.sibling() is not None:
                        v.sibling().color = Color.Red

                if v.isOnLeft():
                    parent.left = None
                else:
                    parent.right = None
            return

        if v.left is None or v.right is None:
            if v is self.root:
                v.data = u.data
                v.left = v.right = None
            else:
                if v.isOnleft():
                    parent.left = u
                else:
                    parent.right = u

                u.parent = parent
                if (uvBlack):
                    self.foixDoubleBlack(u)
                else:
                    u.color = Color.Black
            return
        self.swapValues(u, v)
        self.deleteNode(u)

    def swapValues(self, u, v):
        temp = u.data
        u.data = v.data
        v.data = temp

    def sibling(self):
        if self.parent is None:
            return None
        if (self.isOnLeft()):
            return parent.right
        else:
            return paretn.left

    def isOnLeft(self):
        return self.data == self.parent.left.data

    def hasRedChild(self):
        return True if (self.left is not None and self.left.color is Color.Red) or (
                self.right is not None and self.right.color is Color.Red) else False

    def fixDoubleBlack(self, x):
        if x == self.root:
            return

        sibling = x.sibling()
        parent = s.parent

        if (subling is None):
            self.fixDoubleBlack(parent)
        else:
            if (sibling.color is Color.Red):
                parent.color = Color.Red
                sibling.color = Color.Black
                if sibling.isOnLeft():
                    self.rotateRight(parent)
                else:
                    self.rotateLeft(parent)
                self.fixDoubleBlack(x)
            else:
                if sibling.hasRedChild():
                    if sibling.left is not None and sibling.left.color is Color.Red:
                        if sibling.isOnLeft():
                            sibling.left.color = sibling.color
                            sibling.color = parent.color
                            self.rotateRight(parent)
                        else:
                            sibling.left.color = parent.color
                            self.rotateRight(sibling)
                            self.rotateLeft(parent)
                    else:
                        if sibling.isOnLeft():
                            sibling.right.color = parent.color
                            self.rotateLeft(sibling)
                            self.rotateRight(parent)
                        else:
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            self.rotateLeft(parent)
                    parent.color = Color.Black
                else:
                    sibling.color = Color.Red
                    if parent.color is Color.Black:
                        self.fixDoubleBlack(parent)
                    else:
                        parent.color = Color.Black

    def BSTreplace(self, x):
        if x.left is not None and x.right is not None:
            return self.successor(x.right)

        if x.left is None and x.right is None:
            return None
        if x.left is not None:
            return x.left
        else:
            return x.right

    def successor(self, x):
        temp = x
        while temp.left is not None:
            temp = temp.left
        return temp


if __name__ == "__main__":
    tree = RBTree()
    tree.insert(7)
    tree.insert(6)
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)

    print("InOrder Traversal of Created Tree")
    tree.inOrder(tree.root)
    print("\nLeve Order Traversal of created Tree")
    tree.levelOrder(tree.root)

    tree.deleteByVal(18)
    tree.deleteByVal(11)
    tree.deleteByVal(3)
    tree.deleteByVal(10)
    tree.deleteByVal(22)

    print("InOrder Traversal of Tree After deletion")
    tree.inOrder(tree.root)
    print("\nLeve Order Traversal Tree After deletion")
    tree.levelOrder(tree.root)
