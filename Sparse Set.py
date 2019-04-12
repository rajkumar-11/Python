class SSet:
    def __init__(self, maxV, cap):
        self.maxValue = maxV
        self.capacity = cap
        self.sparse = [0 for i in range(maxV + 1)]
        self.dense = [0 for i in range(cap)]
        self.n = 0

    def insert(self, x):
        if (x > self.maxValue):
            return
        if (self.n >= self.capacity):
            return
        if (self.search(x) is not -1):
            return
        self.dense[self.n] = x
        self.sparse[x] = self.n
        self.n = self.n + 1

    def search(self, x):
        if (x > self.maxValue):
            return -1
        if (self.sparse[x] < self.n and self.dense[self.sparse[x]] == x):
            return self.sparse[x]
        return -1

    def printSet(self):
        for i in range(self.n):
            print(self.dense[i], end=" ")

    def intersect(self, set2):
        cap = min(self.n, set2.n)
        maxVal = min(self.maxValue, set2.maxValue)

        result = SSet(maxVal, cap)
        if (self.n < set2.n):
            for i in range(self.n):
                if (set2.search(self.dense[i]) != -1):
                    result.insert(dense[i])
        else:
            for i in range(set2.n):
                if (self.search(set2.dense[i]) != -1):
                    result.insert(set2.dense[i])

        return result

    def union(self, set2):
        cap = self.n + set2.n
        maxVal = max(self.maxValue, set2.maxValue)

        result = SSet(maxVal, cap)

        for i in range(set2.n):
            result.insert(set2.dense[i])

        for i in range(self.n):
            result.insert(self.dense[i])



        return result

    def deletion(self,x):
        if(self.search(x)==-1):
            return
        temp=self.dense[self.n-1]
        self.dense[self.sparse[x]]=temp
        self.sparse[temp]=self.sparse[x]

        self.n=self.n-1


if __name__ == "__main__":
    set = SSet(100, 5)
    set.insert(5)
    set.insert(3)
    set.insert(9)
    set.insert(10)
    print("Elements in set  are ")
    set.printSet()

    index = set.search(3)
    if (index != -1):
        print(" 3 is found at index= ", index)
    else:
        print("3 doesnot exist in set")
    set.deletion(9)
    set.printSet()

    set2 = SSet(1000, 6)
    set2.insert(4)
    set2.insert(3)
    set2.insert(7)
    set2.insert(200)
    print("\nThe elements in set 2 are", )
    set2.printSet()

    intersect = set2.intersect(set)
    print("\nIntersection of set1 and set 2 is")
    intersect.printSet()
    unionset = set2.union(set)
    print("\nUnion  of set1  and set2  is ")
    unionset.printSet()
