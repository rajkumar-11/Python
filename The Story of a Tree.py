from collections import defaultdict
from fractions import Fraction


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.count = 0
        self.num = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # class Node:
    #     def __init__(self,data):
    #         self.data=data
    #         self.parent=-1


class Graph2:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        # self.count = 0
        # self.num = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)


def udpateParent(graph, parent, u):
    visited = [False] * graph.n
    # visited[u]=True
    updateParentUtils(graph, visited, parent, u)


def updateParentUtils(graph, visited, parent, u):
    visited[u] = True
    for v in graph.graph[u]:
        if visited[v] is False:
            # v.parent = u
            parent[v] = u
            updateParentUtils(graph, visited, parent, v)


def getCount(graph, parent, graph2, u, k):
    visited = [False] * graph.n
    getCountUtils(graph, parent, graph2, visited, u, k)


def getCountUtils(graph, parent, graph2, visited, u, k):
    visited[u] = True

    # count = 0
    # print(parent)
    # if u == 0:
    #     for i in range(len(arr)):
    #         if parent[arr[i][1]] == arr[i][0]:
    #             graph.num = graph.num + 1
    #             count = count + 1

    if u == 0:
        for x in range(graph2.n):
            for v in graph2.graph[x]:
                # print("u= ",u,"  v= ",v)
                if parent[v] == x:
                    graph.num = graph.num + 1

    # print("num= ", graph.num, " k= ", k)

    # else:
    #     for i in graph.graph[u]:
    #         if [u, parent] in arr:
    #             graph.num = graph.num - 1
    # print("num =",graph.num)

    if graph.num >= k:
        graph.count = graph.count + 1
        # print("u= ",u)
    for v in graph.graph[u]:
        if visited[v] is False:
            parent[v] = -1
            parent[u] = v
            s = 0
            # for p in graph.graph[u]:
            #     if [u, p] in arr:
            #         graph.num = graph.num + 1
            #         s = s + 1
            # print("s= ",s)
            num = graph.num
            # print("num inside =", num)

            for x in graph2.graph[u]:
                if x == v:
                    graph.num -= 1
                    s = s + 1
            for x in graph2.graph[v]:
                if x == u:
                    graph.num = graph.num + 1
                    s = s - 1

            # print("s= ", s)

            # if [u, v] in arr:
            #     graph.num -= 1
            #     s = s + 1
            # if [v, u] in arr:
            #     graph.num = graph.num + 1
            #     s = s - 1
            getCountUtils(graph, parent, graph2, visited, v, k)
            parent[u] = -1
            parent[v] = u
            graph.num = num
    # graph.num = graph.num + count


if __name__ == "__main__":
    q = int(input())
    number = 0
    for i in range(q):
        n = int(input())
        graph = Graph(n)
        graph2 = Graph2(n)
        for i in range(n - 1):
            u, v = list(map(int, input().split()))
            graph.addEdge(u - 1, v - 1)
        parent = [-1] * graph.n
        udpateParent(graph, parent, 0)
        g, k = list(map(int, input().split()))
        # pr
        # arr=[[-1 for i in range(2)]for j in range(g)]
        # arr = []
        # print(parent)
        for i in range(g):
            # arr[i][0],arr[i][1]=list(map(int,input().split()))
            # arr[i][0]=arr[i][0]-1
            # arr[i][1] = arr[i][1] - 1
            x, y = list(map(int, input().split()))
            graph2.addEdge(x - 1, y - 1)
            # z = [x - 1, y - 1]
            # arr.append(z)
        # print(parent)
        # print(parent)
        getCount(graph, parent, graph2, 0, k)
        # print("count =", graph.count)
        x = graph.count / graph.n
        if x == 0:
            print("0/1")
        elif x == 1:
            print("1/1")
        else:
            print(Fraction(graph.count, graph.n))
