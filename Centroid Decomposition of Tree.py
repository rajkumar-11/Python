from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.centroidMarked = [False] * (n + 1)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def decomposeTree(self, root):
        centroid = self.getCentroid(root)
        print(centroid, end=" ")

        for i in (self.graph[centroid]):
            if (self.centroidMarked[i] is False):
                centroidSubTree = self.decomposeTree(i)

        return centroid

    def getCentroid(self, src):
        visited = [False] * self.n
        subTree = [0] * self.n
        n = 0
        n=self.DFS(src, visited, subTree, n)
        visited = [False] * (self.n)
        centroid = self.getCentroidUtils(src, visited, subTree, n)
        self.centroidMarked[centroid] = True

        return centroid

    def DFS(self, src, visited, subTree, n):
        visited[src] = True
        n = n + 1
        subTree[src] = 1
        for v in self.graph[src]:
            if visited[v] is False and self.centroidMarked[v] is False:
                n=self.DFS(v, visited, subTree, n)
                subTree[src] = subTree[src] + subTree[v]
        return n

    def getCentroidUtils(self, src, visited, subTree, n):
        isCentroid = True
        visited[src] = True
        heaviestChild = 0
        for v in self.graph[src]:
            if visited[v] is False and self.centroidMarked[v] is False:
                if subTree[v] > n / 2:
                    isCentroid = False
                if heaviestChild == 0 or subTree[v] > subTree[heaviestChild]:
                    heaviestChild = v

        if isCentroid and n - subTree[src] <= n / 2:
            return src
        return self.getCentroidUtils(heaviestChild, visited, subTree, n)


if __name__ == "__main__":
    n = 16
    graph = Graph(n + 1)
    graph.addEdge(1, 4);
    graph.addEdge(2, 4);
    graph.addEdge(3, 4);
    graph.addEdge(4, 5);
    graph.addEdge(5, 6);
    graph.addEdge(6, 7);
    graph.addEdge(7, 8);
    graph.addEdge(7, 9);
    graph.addEdge(6, 10);
    graph.addEdge(10, 11);
    graph.addEdge(11, 12);
    graph.addEdge(11, 13);
    graph.addEdge(12, 14);
    graph.addEdge(13, 15);
    graph.addEdge(13, 16);
    graph.decomposeTree(1)
