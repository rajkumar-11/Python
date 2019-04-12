from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.n=n
        self.graph = defaultdict(list)
        self.cenroidMarked=[False]*(n+1)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def decomposeTree(self,root):

        centroid=getCentroid(root)
        print(centroid,end=" ")

        for i in(self.graph[centroid]):
            if(self.centroidMarked[i] is False):
                centroidSubTree=self.decomposeTree(i)

        return centroid

    def getCentroid(self):
        visited













if __name__=="__main__":
    n=16
    graph= Graph(n)
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


