n, k = map(int, input().split())
DP = [[0] * (k+1) for _ in range(n+1)]

for i in range(k+1):
    DP[0][i] = 1

for i in range(0, n+1):
    for j in range(1, k+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]

print(DP[n][k] % 1000000000)