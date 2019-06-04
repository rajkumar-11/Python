from collections import defaultdict
import heapq
import sys


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.sum = 0
        self.count = 0

    def addEdge(self, u, v, w):
        if v in self.graph[u]:
            return
        self.graph[u].append(Edge(v, w))
        # self.graph[v].append(Edge(u, w))


class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w


class Node:
    def __init__(self, vertex, value):
        self.vertex = vertex
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


def getMinimumTrasformations(graph, s, v,k):
    n = graph.n
    nodes = []
    list = []
    # print("v= ",v)
    for i in range(n):
        node = Node(i, 9999999999)
        nodes.append(node)
        list.append(node)
    nodes[s].value = 0
    list[s].value = 0
    heapq.heapify(list)
    visited = [False] * n
    while (len(list) > 0):
        node = list.pop(0)
        if node.vertex == v:
            break
        # print(node.vertex)
        # print("vertex= ",node.vertex)
        # nodes.remove(node)
        visited[node.vertex] = True
        for edge in graph.graph[node.vertex]:
            # print("value= ",nodes[node.vertex].value)
            if visited[edge.v] is False and nodes[node.vertex].value is not 9999999999 and nodes[edge.v].value > nodes[
                node.vertex].value + edge.w:
                list.remove(nodes[edge.v])
                nodes[edge.v].value = nodes[node.vertex].value + edge.w
                list.append(nodes[edge.v])
        heapq.heapify(list)

    if nodes[s].value is not 9999999999:
        return nodes[v].value
    else:
        return -1


if __name__ == "__main__":
    n, m, k = list(map(int, input().split()))
    x = -1
    y = -1
    graph = Graph(n * m)
    for i in range(n):
        l = input()
        # print("l= ",l)
        for j in range(m):
            index = n * i + j
            # print("index =",index)
            # print(list[j])
            # print("j= ",j)
            if l[j] == 'U':
                # print(l[j])
                index1 = index - n
                if i is not 0:
                    graph.addEdge(index, index1, 0)
                index1 = index + 1
                if j is not m - 1:
                    graph.addEdge(index, index1, 1)
                index1 = index - 1
                if j is not 0:
                    graph.addEdge(index, index1, 1)
                index1 = index + n
                if i is not n - 1:
                    graph.addEdge(index, index1, 1)
            elif l[j] == 'R':
                # print(l[j])
                index1 = index - n
                if i is not 0:
                    graph.addEdge(index, index1, 1)
                index1 = index + 1
                if j is not m - 1:
                    graph.addEdge(index, index1, 0)
                index1 = index - 1
                if j is not 0:
                    graph.addEdge(index, index1, 1)
                index1 = index + n
                if i is not n - 1:
                    graph.addEdge(index, index1, 1)
            elif l[j] == 'D':
                # print(l[j])
                index1 = index - n
                if i is not 0:
                    graph.addEdge(index, index1, 1)
                index1 = index + 1
                if j is not m - 1:
                    graph.addEdge(index, index1, 1)
                index1 = index - 1
                if j is not 0:
                    graph.addEdge(index, index1, 1)
                index1 = index + n
                if i is not n - 1:
                    graph.addEdge(index, index1, 0)
            elif l[j] == 'L':
                # print(l[j])
                index1 = index - n
                if i is not 0:
                    graph.addEdge(index, index1, 1)
                index1 = index + 1
                if j is not m - 1:
                    graph.addEdge(index, index1, 1)
                index1 = index - 1
                if j is not 0:
                    graph.addEdge(index, index1, 0)
                index1 = index + n
                if i is not n - 1:
                    graph.addEdge(index, index1, 1)
            elif l[j] == '*':
                # print(l[j])
                x = i
                y = j

    v = x*m + y
    if (v - 0 > k):
        # print("here v= ", v, "k= ", k)
        print(-1)
    else:
        getMinimumTrasformations(graph, 0, v,k)
        # print("minTransformation= ", minTransformation)
        # if minTransformation > k:
        #     print(-1)
        # else:
        #     print(minTransformation)
