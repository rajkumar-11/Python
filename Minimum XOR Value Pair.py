class TrieNode:
    def __init__(self):
        self.value = 0
        self.child = []
        self.child.append(None)
        self.child.append(None)


root = None
INT_SIZE = 32


def minXOR(arr, n):
    minXor = 99999999999999999
    root = TrieNode()
    insert(root,arr[0])

    for i in range(1, n):
        minXor = min(minXor, minXorUtil(root,arr[i]))
        insert(root,arr[i])

    return minXor


def insert(root,key):
    temp = root
    for i in range(INT_SIZE - 1, 0, -1):
        currentBit = 1 if key & (1 << i) >= 1 else 0
        if (temp is not  None and temp.child[currentBit] is None):
            temp.child[currentBit] = TrieNode()
        temp = temp.child[currentBit]

    temp.value = key


def minXorUtil(root,key):
    temp = root
    for i in range(INT_SIZE - 1, 0, -1):
        currentBit = 1 if key & (1 << i) >= 1 else 0
        if (temp.child[currentBit] is not None):
            temp = temp.child[currentBit]
        elif (temp.child[1 - currentBit] is not None):
            temp = temp.child[1 - currentBit]
    return key ^ temp.value


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    n = len(arr)
    print(minXOR(arr, n))
