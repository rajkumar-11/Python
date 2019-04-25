from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.visited = [False] * n
        self.noOfNodes = 0
        self.count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)


def getCount(graph, e, n, s):
    # visited=[False]*n
    if graph.visited[s] is False:
        graph.visited[s] = True
        for v in graph.graph[s]:
            graph.noOfNodes = 0
            visited = [False] * n
            visited[s] = True
            getNoOfNodes(graph, visited, v)
            if (graph.noOfNodes % 2 is 0 and (n - graph.noOfNodes) % 2 is 0):
                graph.count = graph.count + 1
                graph.removeEdge(s, v)


def getNoOfNodes(graph, visited, u):
    visited[u] = True
    graph.noOfNodes = graph.noOfNodes + 1
    for v in graph.graph[u]:
        if visited[v] is False:
            getNoOfNodes(graph, visited, v)


if __name__ == "__main__":

    n, e = list(map(int, input().split()))
    graph = Graph(n)
    for i in range(e):
        u, v = list(map(int, input().split()))
        graph.addEdge(u - 1, v - 1)
    # count=getCount(graph,e,n,0)
    for i in range(n):
        getCount(graph, e, n, i)
    print(graph.count)
