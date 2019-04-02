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
                root.left.right=search(root.left.right,key)
                if(root.left.right is not None):
                    root.left=rotateLeft(root.left)
            return  root  if root.left is None else rotateRight(root)
    else:
        if root.right is None:
            return root
        else:
            if root.right.key<key:
                root.right.right=search(root.right.right,key)
                root=rotateLeft(root)
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



def deleteKey(root,key):
    if root is None:
        return root
    root=search(root,key)

    if root.key!=key:
        return root
    else:
        if root.left is None:
            return root.right
        else:
            temp=root
            root=search(root.left,key)
            root.right=temp.right
    return root






def preOrder(root):
    if root is None:
        return
    print(root.key, end="  ")
    preOrder(root.left)
    preOrder(root.right)






if __name__=="__main__":
    root=  Node(6)
    root.left=Node(1)
    root.right=Node(9)
    root.left.right=Node(4)
    root.left.right.left=Node(2)
    root.right.left=Node(7)

    key=4
    root= deleteKey(root,key)
    print("Preorder traversal of modified tree is ")
    preOrder(root)

