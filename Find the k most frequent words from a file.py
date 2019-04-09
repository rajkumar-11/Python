class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.array = []
        for i in range(capacity):
            self.array.append(minHeapNode())


class minHeapNode:
    def __init__(self):
        self.root = None
        self.frequency = 0
        self.word = None


class Node:
    def __init__(self):
        self.isEnd = False
        self.frequency = 0
        self.indexMinHeap = -1
        self.child = []
        for i in range(26):
            self.child.append(None)


def insertTrieAndHeap(word, root, heap, len, index):
    if root is None:
        root = Node()

    if (len != index):
        # print("word[index]-97 =",ord(word[index])-97)
        insertTrieAndHeap(word,root.child[ord(word[index])-97], heap, len, index + 1)
    else:
        if (root.isEnd):
            root.frequency = root.frequency + 1
        else:
            root.isEnd = True
            root.frequency = 1
        insertInMinHeap(heap, root, word)


def insertInMinHeap(heap, root, word):
    # print("indexMin= ",root.indexMinHeap)
    if root.indexMinHeap != -1:
        heap.array[root.indexMinHeap].frequency += 1
        minHeapify(heap, root.indexMinHeap)
    elif (heap.count < heap.capacity):
        count=heap.count
        heap.array[count].frequency = root.frequency
        heap.array[count].word = word
        heap.array[count].root = root
        root.indexMinHeap = heap.count
        heap.count += 1
        buildMinHeap(heap)
    elif (root.frequency > heap.array[0].frequency):
        heap.array[0].root.indexMinHeap = -1
        heap.array[0].root = root
        heap.array[0].root.indexMinHeap = 0
        heap.array[0].frequency = root.frequency
        minHeapify(heap, 0)


def buildMinHeap(heap):
    n = heap.count - 1
    for i in range(int((n - 1) / 2), 0, -1):
        minHeapify(heap, i)


def minHeapify(heap, index):
    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index
    if (left < heap.count and heap.array[left].frequency < heap.array[smallest].frequency):
        smallest = left
    if (right < heap.count and heap.array[right].frequency < heap.array[smallest].frequency):
        smallest = right
    if (smallest != index):
        heap.array[smallest].root.indexMinHeap = index
        heap.array[index].root.indexMinHeap = smallest
        swapMinHeapNodes(heap, smallest, index)
        minHeapify(heap, smallest)


def swapMinHeapNodes(heap, smallest, index):
    temp = heap.array[smallest]
    heap.array[smallest] = heap.array[index]
    heap.array[index] = temp


def printKMostFreq(file, k):
    heap = MinHeap(k)
    root = None
    for line in file:
        for word in line.split():
            insertTrieAndHeap(word, root, heap, len(word) - 1, 0)

    displayMinHeap(heap)

def displayMinHeap(heap):

    for i in range(heap.count):
        print(heap.array[i].word," ",heap.array[i].frequency)


if __name__ == "__main__":
    k = 5
    file = list(open("C:\\Users\\navhalr\\Desktop\\abc.txt"))
    # print(len(file))
    # for line in file:
    #     for word in line.split():
    #         print(word)
    #     print(file[i])
    if file is None:
        print("File doesnt exist")
    else:
        printKMostFreq(file, k)
