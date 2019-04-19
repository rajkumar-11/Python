class DLLNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class myStack:
    def __init__(self):
        self.count=0
        self.head=None
        self.mid=None

    def push(self,data):
        node=DLLNode(data)
        node.next = self.head
        if self.head is None:
            self.head=node
            self.mid=node
            self.count=1
            return
        if self.count==1:
            self.head.prev=node
            self.head=node
            self.count+=1
            return
        self.head.prev=node
        self.head=node
        self.count=self.count+1
        # print("count= ",self.count," data =",data)
        if(self.count%2 is not 0):
            # print("here")
            self.mid=self.mid.prev

    def pop(self):
        if self.count is 0:
            print("stack is empty")
            return
        node=self.head
        self.head=self.head.next
        self.count=self.count-1

        if(self.count%2 is 0):
            self.mid=self.mid.next
        return node.data

    def findMiddle(self):
        if self.mid is None:
            print("Mid is none here")
            return
        return self.mid.data


if __name__=="__main__":
    mystack=myStack()
    mystack.push(11)
    mystack.push(22)
    mystack.push(33)
    mystack.push(44)
    mystack.push(55)
    mystack.push(66)
    mystack.push(77)
    print("Item poped is ",mystack.pop())
    print("Item poped is ", mystack.pop())
    print("Item poped is ", mystack.findMiddle())

