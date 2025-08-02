def solution(n):
    answer = 0
    
    left = 1
    right = 1
    s = 1
    
    ## 투포인터
    while left <= n:
        if s == n:
            answer += 1
            s -= left
            left += 1
        elif s < n:
            right += 1
            s += right
        else: ## s > n
            s -= left
            left += 1
    
    return answer