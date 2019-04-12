import heapq
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.data < other.data




def printSortedArr(arr,n):
    root=buildCartesianTree(arr,n)
    print("The sorted array is ")
    pQBasedTraversal(root)

def pQBasedTraversal(root):
    list=[]
    list.append(root)
    heapq.heapify(list)
    while(len(list) is not 0):
        top=heapq.heappop(list)
        print(top.data,end=" ")
        if(top.left is not None):
            heapq.heappush(list,top.left)
        if (top.right is not None):
            heapq.heappush(list, top.right)

    return





def buildCartesianTree(arr, n):
    parent = [-1] * n
    left = [-1] * n
    right = [-1] * n

    root = 0
    last = None
    for i in range(1, n):
        last = i - 1
        right[i] = -1
        while (arr[last] >= arr[i] and last != root):
            last = parent[last]

        if (arr[last] >= arr[i]):
            parent[root] = i
            left[i] = root
            root = i
        elif right[last] == -1:
            right[last] = i
            parent[i] = last
            left[i] = -1
        else:
            parent[right[last]] = i
            left[i] = right[last]
            right[last] = i
            parent[i] = last

    parent[root] = -1
    return (buildCartesianTreeUtil(root, arr, parent, left, right))


def buildCartesianTreeUtil(root, arr, parent, left, right):
    if root == -1:
        return None
    node = Node(arr[root])
    node.left = buildCartesianTreeUtil(left[root], arr, parent, left, right)
    node.right = buildCartesianTreeUtil(right[root], arr, parent, left, right)
    return node


if __name__ == '__main__':
    # Assume that inorder traversal of
    # following tree is given
    #    40
    # / \
    # 10     30
    # /      \
    # 5       28

    arr = [5, 10, 40, 30, 28,66,89,45]
    n = len(arr)
    printSortedArr(arr,n)