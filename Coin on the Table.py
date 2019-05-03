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




if __name__=="__main__":
    n,m,k=list(map(int,input().split()))
    l=list(input().split())

