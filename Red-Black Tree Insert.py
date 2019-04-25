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
        # print("node color ", node.color)
        # print("data ",node.data)
        # if node.parent is not None:
        #     print("parent node color ", node.parent.color)

        # print("parent node color ",node.parent.color)
        print("data= ",node.data,"root= ",root.data)

        while (node != root and node.color != Color.Black and node.parent.color == Color.Red):
            parent = node.parent
            print("parent = ", node.parent.data, "color =", node.parent.color)
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


if __name__ == "__main__":
    tree = RBTree()
    tree.insert(77)
    tree.insert(0)
    tree.insert(1)
    tree.insert(11)
    tree.insert(35)
    tree.insert(2)
    tree.insert(1000)
    tree.insert(9)
    tree.insert(13)
    tree.insert(87)


    print("InOrder Traversal of Created Tree")
    print("root=", tree.root.data)
    tree.inOrder(tree.root)
    print("\nLeve Order Traversal of created Tree")
    print("root2=", tree.root.data)
    tree.levelOrder(tree.root)
