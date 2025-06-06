def solution(numbers, target):
    answer = 0
    
    def dfs(idx, current_sum):
        if idx >= len(numbers):
            return 1 if current_sum == target else 0
        return dfs(idx+1, current_sum+numbers[idx]) + dfs(idx+1, current_sum-numbers[idx])
    
    answer = dfs(0,0)
    return answer