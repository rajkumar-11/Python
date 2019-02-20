class MyClass:
    __hiddenVariable=0
    def add(self,increment):
        self.__hiddenVariable+=increment
        print(self.__hiddenVariable)

obj= MyClass()
# obj.add(2)
# obj.add(5)

print(obj._MyClass__hiddenVariable)