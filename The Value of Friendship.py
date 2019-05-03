from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


class Node:
    def __init__(self, data):
        self.count = 0
        self.data = data


def getCount(graph, visite, u, v):
    # visited=[False]*graph.n
    count = 0

    for i in range(graph.n):
        if visited[i] is False:
            graph.count = 0
            getCountUtils(graph, visited, i)
            # print("count= ",graph.count)
            count += graph.count * (graph.count - 1)

    # print("count before sending ",count)
    return count


def find(graph, parent, u):
    if parent[u] != u:
        parent[u]=find(graph,parent,parent[u])
    return parent[u]


# def findParent(graph, parent, noOfNodes, sum, u):
#     if parent[u] == u:
#         noOfNodes[u] = sum
#         return u
#     else:
#         noOfNodes[u] = sum
#         findParent(graph, parent, noOfNodes, sum, parent[u])


def union(graph, u, v, parent, rank):
    x = noOfNodes[u] + noOfNodes[v]
    # print("sum= ", x)
    # a = findParent(graph, parent, noOfNodes, x, u)
    # b = findParent(graph, parent, noOfNodes, x, v)
    a = find(graph, parent, u)
    b = find(graph, parent, v)
    # print("a =",a," b= ",b)
    # x = noOfNodes[u] + noOfNodes[v]
    # noOfNodes[a] = x
    # noOfNodes[b] = x
    # parent[x] = y
    if rank[a] > rank[b]:
        parent[b] = a
        # child[a] = b
    elif rank[b] > rank[a]:
        parent[a] = b
        # child[b] = a
    else:
        parent[a] = b
        # child
        rank[b] = rank[b] + 1
    return x


def getCountUtils(graph, visited, u):
    visited[u] = True
    graph.count += 1
    for v in graph.graph[u]:
        if visited[v] is False:
            getCountUtils(graph, visited, v)


def updateGraphNoOfNodes(graph, sum, noOfNodes, u):
    visited = [False] * graph.n
    updateGraphNoOfNodesUtils(graph, visited, sum, noOfNodes, u)


def updateGraphNoOfNodesUtils(graph, visited, sum, noOfNodes, u):
    visited[u] = True
    noOfNodes[u] = sum

    for v in graph.graph[u]:
        if visited[v] is False:
            # print("$###################", v)
            updateGraphNoOfNodesUtils(graph, visited, sum, noOfNodes, v)


if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        count = 0
        num = 0
        n, m = list(map(int, input().split()))
        graph = Graph(n)
        parent = [-1] * graph.n
        for i in range(graph.n):
            parent[i]=i
        child = [-1] * graph.n
        noOfNodes = [1] * graph.n
        rank = [0] * graph.n
        # print("yes")
        for j in range(m):
            # print("j ",j," m ",m)
            x, y = list(map(int, input().split()))
            #     visited = [False] * graph.n
            #     graph.addEdge(x - 1, y - 1)
            #     # count+=getCount(graph,0)
            #     count = getCount(graph, visited, x - 1, y - 1)
            #     # print(count)
            # print(count)
            # parent = []
            # noOfNodes = []
            # print("x= ", x, "y= ", y, " n=", n)
            graph.addEdge(x - 1, y - 1)
            # parent[x - 1] = x - 1
            # parent[y - 1] = y - 1
            a = find(graph, parent, x - 1)
            b = find(graph, parent, y - 1)

            if a == b:
                # num = num + noOfNodes[x - 1] * noOfNodes[x - 1] - 1
                # print("hereDisjoint Set (Or Union-Find) | Set 1")
                # print("num= ", num)
                count = count + num
            else:
                # print("x ", x - 1, " y", y - 1)

                union(graph, x - 1, y - 1, parent, rank)
                # print("nodes x", noOfNodes[x - 1], " nodes y", noOfNodes[y - 1])
                sum=noOfNodes[x-1]+noOfNodes[y-1]
                num+=noOfNodes[x-1]*noOfNodes[y-1]*2
                # print("sum= ", sum)
                # print(noOfNodes)
                updateGraphNoOfNodes(graph, sum, noOfNodes, x - 1)
                # print("x nodes= ", noOfNodes[x - 1], " y nodes ", noOfNodes[y - 1])
                # print(noOfNodes)
                # num =  noOfNodes[x - 1] * (int(noOfNodes[x - 1]) - 1)

                # num = num + noOfNodes[x - 1] * noOfNodes[y - 1]
                # print("num= ", num)
                # noOfNodes[x - 1] = noOfNodes[x - 1] + noOfNodes[y - 1]
                # noOfNodes[y - 1] = noOfNodes[x - 1] + noOfNodes[y - 1]
                count = count + num
        print(count)
