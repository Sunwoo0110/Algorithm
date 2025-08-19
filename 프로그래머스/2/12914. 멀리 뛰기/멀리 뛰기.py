def solution(n):
    answer = 0
    
    dp = [0 for _ in range(n+2)]
    dp[0] = 1
    dp[1] = 1
    
    for i in range(n):
        dp[i+2] = dp[i]+dp[i+1]
        
    answer = dp[n]%1234567
    
    return answer