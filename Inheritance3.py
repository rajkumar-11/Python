class Base:
    def __init__(self,x):
        self.x=x

class Derived(Base):

    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def printXY(self):
        print(self.x, self.y)

d= Derived(10,20)
d.printXY()