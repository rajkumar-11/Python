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


def getMinimumEdgesToReverse(graph, s, v):
    n = graph.n
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
    graph = Graph(7)
    graph.addEdge(0, 1, 0)
    graph.addEdge(2, 1, 0)
    graph.addEdge(2, 3, 0)
    graph.addEdge(5, 1, 0)
    graph.addEdge(6, 4, 0)
    graph.addEdge(6, 3, 0)
    graph.addEdge(1, 0, 1)
    graph.addEdge(1, 2, 1)
    graph.addEdge(3, 2, 1)
    graph.addEdge(1, 5, 1)
    graph.addEdge(4, 6, 1)
    graph.addEdge(3, 6, 1)

    minEdgesToReverse = getMinimumEdgesToReverse(graph, 0, 6)

    if minEdgesToReverse != -1:
        print(minEdgesToReverse)
    else:
        print("Not possible")
