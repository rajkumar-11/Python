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
        self.graph[v].append(Edge(u, w))


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


def findMinimumDistance(graph, n, m, s):
    nodes = []
    list = []
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
    dist = []
    for i in range(n):
        if nodes[i].value == 9999999999:
            dist.append(-1)
        else:
            dist.append(nodes[i].value)
    return dist


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().split()))
        graph = Graph(n)
        for j in range(m):
            u, v, w = list(map(int, sys.stdin.readline().split()))
            graph.addEdge(u - 1, v - 1, w)
        s = int(input())
        minDistance = findMinimumDistance(graph, n, m, s - 1)
        for i in range(n):
            if i == s - 1:
                continue
            print(minDistance[i], end=" ")
        print()
