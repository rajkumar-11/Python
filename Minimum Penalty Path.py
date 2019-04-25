from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.n=n
        self.graph=defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append(Edge(v,w))
        self.graph[v].append(Edge(u,w))
        # self.graph[u].append([v,w])
        # self.graph[u].append([u, w])

class Edge:
    def __init__(self,v,w):
        self.v=v
        self.w=w


if __name__=="__main__":
    n,m= list(map(int,input().split()))
    graph=Graph(n)
    for i in range(m):
        x,y,c=list(map(int,input().split()))
        graph.addEdge(x-1,y-1,c)
    a,b=list(map(int,input().split()))
    were=[[False for i in range(1024)]for j in range(n)]
    were[a-1][0]=True
    BFS=[]
    BFS.append(a-1)
    k=[]
    k.append(0)
    while(len(BFS) is not 0):
        i=BFS.pop(0)
        j=k.pop(0)
        for x in graph.graph[i]:
            if (were[x.v][j|x.w] is False):
                were[x.v][j|x.w] =True
                BFS.append(x.v)
                k.append(j|x.w)

    for i in range(1024):
        if were[b-1][i]==True:
            print(i)
            break










