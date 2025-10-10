def solution(alp, cop, problems):
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[float('inf')] * (max_cop+2) for _ in range(max_alp+2)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            ## 공부로 +1
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            ## 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    ni = min(max_alp, i+alp_rwd)
                    nj = min(max_cop, j+cop_rwd)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j]+cost)

    return dp[max_alp][max_cop]
