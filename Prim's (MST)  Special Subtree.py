from collections import defaultdict
import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.weight=0


    def addEdge(self,u,v,w):
        self.graph[u].append(Edge(v,w))
        self.graph[v].append(Edge(u,w))


class Edge:
    def __init__(self,v,w):
        self.v=v
        self.w=w


class Node:
    def __init__(self,vertex):
        self.vertex=vertex
        self.value=999999999999999999999999999
    def __lt__(self,other):
        return self.value<other.value



def getPrimsMST(graph,u):
    list=[]
    nodes=[]
    for i in range(graph.n):
        node=Node(i)
        list.append(node)
        nodes.append(node)
    node=list[u]
    list.remove(node)
    node.value=0
    list.append(node)
    heapq.heapify(list)
    visited=[False]*graph.n
    result=0
    key=[999999999]*graph.n
    key[u]=0


    while(len(list) is not 0):
        node=list[0]
        # print(node.value)
        result=result+node.value
        list.remove(node)
        visited[node.vertex] = True
        for x in graph.graph[node.vertex]:
            # print("v= ",x.v)
            if visited[x.v] is False and x.w<nodes[x.v].value:
                # print("size before= ",len(list))
                list.remove(nodes[x.v])
                # print("size after= ", len(list))
                nodes[x.v].value=x.w
                list.append(nodes[x.v])
                heapq.heapify(list)
    return result




if __name__ == "__main__":

    n, m = list(map(int, input().split()))
    graph = Graph(n)
    for i in range(m):
        x, y, c = list(map(int, input().split()))
        graph.addEdge(x - 1, y - 1, c)
    s=int(input())
    # print(graph.weight)
    print(getPrimsMST(graph,s-1))


