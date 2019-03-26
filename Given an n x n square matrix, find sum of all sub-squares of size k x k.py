M = 4
N = 5
def findCommon(mat):
    last_index=[N-1]*M
    min_row=0

    while last_index[min_row]>=0:
        # print(last_index)
        for i in range(0,M):
            # print("values= ",mat[i][last_index[i]])
            if (mat[i][last_index[i]]<mat[min_row][last_index[min_row]]):
                min_row=i
                print("here")

        count=0;
            # print("minimum row =",min_row)

        for i in range(M):
            if (mat[i][last_index[i]] > mat[min_row][last_index[min_row]]):
                if (last_index[i] == 0):
                    return -1;
                last_index[i] -= 1
            else:
                count = count + 1;
        # print("count =",count)

        if count == M:
            return mat[min_row][last_index[min_row]]
    return -1

if __name__ == "__main__":

    mat = [[1, 2, 3, 4, 5],
           [2, 4, 5, 8, 10],
           [3, 5, 7, 9, 11],
           [1, 3, 5, 7, 9]]

    result = findCommon(mat)
    if (result == -1):
        print("No common element")
    else:
        print("Common element is", result)