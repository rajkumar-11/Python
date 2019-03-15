class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enQueue(self, a):
        self.stack1.append(a)

    def deQueue(self):

        if len(self.stack1) is 0 and len(self.stack2) is 0:
            print("Both stacks are empty  Not Possible")
            return

        if (len(self.stack1) is not 0):
            while(len(self.stack1) is not 0):
                self.stack2.append(self.stack1.pop())

        x=self.stack2.pop()
        return x

if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(6)
    q.enQueue(7)
    q.enQueue(8)
    q.enQueue(9)
    q.enQueue(10)
    q.enQueue(11)


    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

