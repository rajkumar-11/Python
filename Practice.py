class Node:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def chageTheValueForB(node):
    node.b=15
    return

if __name__=="__main__":
    node=Node(5,10)
    chageTheValueForB(node)
    print("a= ",node.a,"b= ",node.b)

