class Candle:
    def __init__(self, h, c):
        self.height = h
        self.color = c


def getCount(candles, n, k):
    temp = [1 for i in range(n)]
    sets = [set() for i in range(n)]
    for i in range(n):
        sets[i].add(candles[i].color)
    count = 0
    # print("n= ",n," k= ",k)

    for i in range(1, n):
        for j in range(0, i):
            if candles[i].height > candles[j].height and temp[i] < temp[j] + 1:
                temp[i] = temp[j] + 1
                sets[i] = sets[j]
                sets[i].add(candles[i].color)
                # print("here")
                # print("len= ",len(sets[i]))
                if len(sets[i]) >= k:
                    count = count + 1
    return count


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    candles = [None for i in range(n)]
    for i in range(n):
        h, c = list(map(int, input().split()))
        candles[i] = Candle(h, c)
    count = getCount(candles, n, k)
    print(count)
