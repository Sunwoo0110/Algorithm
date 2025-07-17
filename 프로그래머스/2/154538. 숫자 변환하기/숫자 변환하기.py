def solution(x, y, n):
    answer = 0
    dp = [-1 for _ in range(y+1)]
    dp[x] = 0
    
    for i in range(x, y+1):
        if dp[i] == -1:
            continue
            
        if i+n <= y:
            dp[i+n] = min(dp[i]+1, dp[i+n]) if dp[i+n] != -1 else dp[i]+1
        if i*2 <= y:
            dp[i*2] = min(dp[i]+1, dp[i*2]) if dp[i*2] != -1 else dp[i]+1
        if i*3 <= y:
            dp[i*3] = min(dp[i]+1, dp[i*3]) if dp[i*3] != -1 else dp[i]+1
    
    return dp[y]