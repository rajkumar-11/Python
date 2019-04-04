class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isPairPresent(root,target):
    arr=[]
    inorder(root,arr)
    # print(len(arr))
    start=0
    end=len(arr)-1

    while(start<end):
        if arr[start]+arr[end]==target:
            print("indexes for the given target are ",start," ",end)
            return
        elif arr[start]+arr[end]>target:
            end=end-1
        else:
            start=start+1
    print("Not present ")




def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)









if __name__=="__main__":
    root=Node(15)
    root.left=Node(10)
    root.right=Node(20)
    root.left.left=Node(8)
    root.left.right=Node(12)
    root.right.left=Node(16)
    root.right.right=Node(25)

    isPairPresent(root,33)