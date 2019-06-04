if __name__ == "__main__":
    M, N = list(map(int, input().split()))
    # N=int(input())
    arr = [[0 for i in range(N)] for j in range(M)]
    for i in range(M):
        arr[i] = list(map(int, input().split()))
    result = 0;
    result = result + M * N * 2
for i in range(N):
    result += arr[0][i] + arr[M - 1][i]

for i in range(M):
    result += arr[i][0] + arr[i][N - 1]

# for i in range(N - 1):
#     for j in range(M):
#         result += abs(arr[i + 1][j] - arr[i][j])
#
# for i in range(M - 1):
#     for j in range(N):
#         result += abs(arr[j][i+1] - arr[j][i])


for i in range(M-1):
    for j in range(N):
        result+=abs(arr[i+1][j]-arr[i][j])


for  j in range(N-1):
    for i in range(M):
        result+=abs(arr[i][j+1]-arr[i][j])

print(result)

