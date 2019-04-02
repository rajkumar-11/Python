class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


def search(root,key):

    if root is None or root.key== key:
        return root

    if(root.key>key):
        if(root.left is None):
            return root
        else:
            if root.left.key>key:
                root.left.left=search(root.left.left,key)
                root=rotateRight(root)
            elif root.left.key<key:
                root.left.right=search(root.left.right.right,key)
                if(root.left.right is not None):
                    root.left=rotateLeft(root.left)
            return  root  if root.left is None else rotateRight(root)
    else:
        if root.right is None:
            return root
        else:
            if root.right.key<key:
                root.right.right=search(root.right.right,key)
                root=rotateLeft(root,key)
            elif root.right.key>key:
                root.right.left= search(root.right.left,key)
                if(root.right.left is not None):
                    root.right=rotateRight(root.right)
        return root if root.right is None else rotateLeft(root)

def rotateLeft(z):
    y=z.right
    T2=y.left
    #Rotate
    y.left=z
    z.right=T2
    return y

def rotateRight(x):
    z=x.left
    T2=z.right

    #Rotate
    z.right=x
    x.left=T2
    return z





def preOrder(root):
    if root is None:
        return
    print(root.key, end="  ")
    preOrder(root.left)
    preOrder(root.right)






if __name__=="__main__":
    root=  Node(100)
    root.left=Node(50)
    root.right=Node(200)
    root.left.left=Node(40)
    root.left.left.left=Node(30)
    root.left.left.left.left=Node(20)

    root=search(root,20)
    print("Preorder traversal of modified tree is ")
    preOrder(root)

