def findMethodNum(n):
    DP = [0] * (10 + 1)
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4
    
    for i in range(4, n+1):
        DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
    
    return DP[n]

tc_num = int(input())

for i in range(tc_num):
    num = int(input())
    print(findMethodNum(num))