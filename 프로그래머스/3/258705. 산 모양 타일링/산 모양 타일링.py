def solution(n, tops):
    answer = 0
    MOD = 10007
    
    # dp[i][0] : i번째까지 채운 상태, 오른쪽 안채움
    # dp[i][1] : i번째까지 채운 상태, 오른쪽 채움
    dp = [[0, 0] for _ in range(n)]
    
    if tops[0] == 1:
        dp[0][0] = 3
        dp[0][1] = 1
    else:
        dp[0][0] = 2
        dp[0][1] = 1
    
    for i in range(1, n):
        if tops[i] == 0:
            dp[i][0] = (dp[i-1][0]*2 + dp[i-1][1]) % MOD
        else:
            dp[i][0] = (dp[i-1][0]*3 + dp[i-1][1]*2) % MOD
        
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD
    
    answer = (dp[n-1][0] + dp[n-1][1]) % MOD
    return answer
