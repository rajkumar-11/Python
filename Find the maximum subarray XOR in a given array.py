class TrieNode:
    def __init__(self):
        self.value = 0
        self.child = []
        self.child.append(None)
        self.child.append(None)

INT_SIZE=32
root=None



def maxSubArrayXOR(arr,n):
    root=TrieNode()
    insert(root,0)
    result=-999999999
    preXor=0
    for i in range(n):
        preXor=preXor^arr[i]
        insert(root,preXor)
        result=max(result,query(root,preXor))

    return result

def insert(root,preXor):
    temp=root
    for i in range(INT_SIZE-1,-1,-1):
        val=1 if (preXor & 1<<i)>=1 else 0
        if (temp.child[val] is None):
            temp.child[val]=TrieNode()
        temp=temp.child[val]

    temp.value=preXor

def query(root,preXor):
    temp=root
    for i in range(INT_SIZE-1,-1,-1):
        val = 1 if (preXor & 1 << i) >= 1 else 0
        if(temp.child[1-val] is not None):
            temp=temp.child[1-val]
        elif(temp.child[val] is not None):
            temp=temp.child[val]

    return preXor^temp.value




if __name__=="__main__":
    arr=[8,1,2,12]
    n=len(arr)
    print("Max subarray XOR is ",maxSubArrayXOR(arr,n))