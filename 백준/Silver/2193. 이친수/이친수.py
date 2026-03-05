num = int(input())
DP = [[0] * 2 for _ in range(num+1)]
DP[1][0] = 0
DP[1][1] = 1

for i in range(2, num+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0]
    
print(sum(DP[num]))