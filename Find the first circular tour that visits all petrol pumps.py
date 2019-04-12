class PetrolPump:

    # Constructor to create a new node
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance

def printTour(arr):
    start=0
    end=len(arr)
    n=len(arr)
    curr_oil=0
    index=0
    # print("start ",start," end ",end)

    while(start!=end):
        # print("start =",start)
        curr_oil=arr[start].petrol-arr[start].distance
        # print("curr_oil ",curr_oil)
        index=(start+1)%n
        while(index !=start and curr_oil>=0):
            curr_oil=arr[index].petrol-arr[index].distance
            index=(index+1)%n
        if index==start:
            return start
        start=(start+1)
    return -1






if __name__=="__main__":
    arr = [PetrolPump(6, 4), PetrolPump(1, 6), PetrolPump(7, 3)]
    start = printTour(arr)
    print("No solution" if start == -1 else "start will be from =", start)