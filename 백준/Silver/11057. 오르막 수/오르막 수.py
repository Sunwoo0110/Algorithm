num = int(input())
DP = [[0] * 10 for _ in range(num+1)]

for i in range(10):
    DP[1][i] = 1
    
for i in range(2, num+1):
    for j in range(10):
        for k in range(j, 10):
            DP[i][j] = DP[i][j] + DP[i-1][k]
        
print(sum(DP[num])%10007)