from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.sum=0
        self.count=0

    def addEdge(self, u, v, w):
        self.graph[u].append(Edge(v, w))
        self.graph[v].append(Edge(u, w))


class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w


def DFS(graph, u, nodes):
    visited = [False] * graph.n
    value = [0] * graph.n
    DFSUtil(graph, visited, value, u, 0)
    sum = 0
    # print(value)
    for i in range(1, len(nodes)):
        sum += value[nodes[i] - 1]
    print(sum)


def DFSUtil(graph, visited, value, u, sum):
    value[u] = sum
    visited[u] = True

    for node in graph.graph[u]:
        if visited[node.v] == False:
            DFSUtil(graph, visited, value, node.v)


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    nodes = list(map(int, input().split()))

    graph = Graph(n)
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        graph.addEdge(u - 1, v - 1, w)
    DFS(graph, nodes[0] - 1, nodes)
