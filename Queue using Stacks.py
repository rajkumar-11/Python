
class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enQueue(self,a):
        while len(self.stack1) is not 0:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(a)
        while(len(self.stack2) is not 0):
            self.stack1.append(self.stack2.pop())

    def deQueue(self):
        if(len(self.stack1)==0):
            return -1
        return self.stack1.pop();

if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(6)
    q.enQueue(7)
    q.enQueue(8)
    q.enQueue(9)


    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

