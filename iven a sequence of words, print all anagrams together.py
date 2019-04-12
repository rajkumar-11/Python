class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.head = []
        self.child = []
        for i in range(26):
            self.child.append(None)


def printAnagramsTogether(wordArr, n):
    root = None
    for i in range(n):
        word = wordArr[i]
        word = ''.join(sorted(word))
        # print(word)
        root = insert(root, word, i, 0)
    printAnagramsUtil(root,wordArr)


def printAnagramsUtil(root,WordArr):
    if root is None:
        return
    if root.isEnd:
        for x in root.head:
            print(WordArr[x],end=" ")
    else:
        for i in range(26):
            printAnagramsUtil(root.child[i],wordArr)

def insert(root, word, i, index):
    if root is None:
        root = TrieNode()

    # print("index= ",index)

    if (len(word)> index):
        root.child[ord(word[index]) - 97] = insert(root.child[ord(word[index]) - 97], word, i, index + 1)
    else:
        if (root.isEnd):
            root.head.append(i)
        else:
            root.isEnd = True
            root.head.append(i)
    return root


if __name__ == "__main__":
    wordArr = ["cat", "dog", "tac", "god", "act", "gdo"]
    printAnagramsTogether(wordArr, len(wordArr))
