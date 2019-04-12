class Heap:
    def __init__(self, N):
        self.capacity = N
        self.count = 0
        self.array = []
        # for i in range(N):
        #     self.array.append(Node(None, None))


class Node:
    def __init__(self, data, list):
        self.data = data
        self.list = list


def externalSort(list, N):
    heap = Heap(N)
    buildHeap(heap, list, N)
    # for i in range(heap.count):
    #     print(heap.array[i].data)
    # for i in range(heap.count):
    #     print(heap.array[i].data)
    while (heap.count > 0):
        # print("count= ", heap.count)
        print(heap.array[0].data,end=" ")
        extractMinimum(heap, list, N)


def extractMinimum(heap, listList, N):
    if heap.count == 0:
        return
    list = heap.array[0].list
    # print("list =" ,list)
    # print("len =", len(listList[list]))

    if (len(listList[list]) is not  0):
        heap.array[0].data = listList[list].pop(0)
        heap.array[0].list=list
        minHeapify(heap, 0, heap.count)
    else:

        heap.array[0].data = heap.array[heap.count - 1].data
        heap.array[0].list=heap.array[heap.count - 1].list
        heap.count = heap.count - 1
        minHeapify(heap, 0, heap.count)


def buildHeap(heap, list, N):
    for i in range(N):
        node=Node(list[i].pop(0),i)
        heap.array.append(node)
        # print("data =", heap.array[i].data)
        heap.count = heap.count + 1;
    Heapify(heap, heap.count)


def minHeapify(heap, i, N):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < N and heap.array[smallest].data > heap.array[left].data):
        smallest = left
    if (right < N and heap.array[smallest].data > heap.array[right].data):
        smallest = right
    if smallest != i:
        temp = heap.array[smallest]
        heap.array[smallest] = heap.array[i]
        heap.array[i] = temp
        minHeapify(heap, smallest, N)


def Heapify(heap, N):
    # print("N= ",N)
    for i in range(int((N -1)/ 2 ), -1, -1):
        # print("i= ",i)
        minHeapify(heap, i, heap.count)


if __name__ == "__main__":
    N = 3
    list = []
    list1 = []
    list2 = []
    list3 = []
    list1.append(30)
    list1.append(40)
    list1.append(50)
    list2.append(35)
    list2.append(45)
    list2.append(55)
    list2.append(65)
    list3.append(10)
    list3.append(60)
    list3.append(70)
    list3.append(80)
    list3.append(100)

    list.append(list1)
    list.append(list2)
    list.append(list3)

    externalSort(list, N)
