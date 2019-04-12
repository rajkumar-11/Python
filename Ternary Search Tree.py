class Node:
    def __init__(self, data):
        self.data = data
        self.isEndOfString = 0
        self.left = None
        self.right = None
        self.eq = None


def insert(root, word):
    # print(len(word))
    # if len(word)<=0:
    #     return root

    if root is None:
        root = Node(word[0])

    if word[0] < root.data:
        root.left = insert(root.left, word)
    elif (word[0] > root.data):
        root.right = insert(root.right, word)
    else:
        if len(word) > 1:
            # print("len(word)= ",len(word))
            root.eq = insert(root.eq, word[1:])
        else:
            root.isEndOfString = 1
    return root


def traverseTSTUtil(root, buffer, depth):
    # print("bac")
    # print(root)
    # print("buffer =",buffer)
    if not (root is None):
        # print("dafsd")
        traverseTSTUtil(root.left, buffer, depth)
        buffer[depth] = root.data
        if root.isEndOfString == 1:
            # print("x")
            buffer[depth + 1] = '\0'
            print(buffer)
        traverseTSTUtil(root.eq, buffer, depth + 1)
        traverseTSTUtil(root.right, buffer, depth)
        # buffer.pop()


def traverseTST(root):
    buffer = [None] * 50
    traverseTSTUtil(root, buffer, 0)


def searchTST(root, word):
    if root is None:
        return False
    if word[0] < root.data:
        return searchTST(root.left, word)
    elif word[0] > root.data:
        return searchTST(root.right, word)
    else:
        if len(word) == 1:
            return True if root.isEndOfString == 1 else False
        return searchTST(root.eq, word[1:])


if __name__ == "__main__":
    root = None
    root = insert(root, "cat")
    root = insert(root, "cats")
    root = insert(root, "navhal")
    root = insert(root, "ozil")
    print("Following is the traversal of ternary search Tree")
    traverseTST(root)
    # print("Following are search results for cats,bu and cat respectively\n")
    if searchTST(root, "navhal") == True:
        print("Found")
    else:
        print("Not Found")
