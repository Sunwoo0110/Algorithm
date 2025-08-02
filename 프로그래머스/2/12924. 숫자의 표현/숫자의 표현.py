def solution(n):
    answer = 0
    
    left = 1
    right = 1
    s = 1
    
    while left <= right:
        while True:       
            if s >= n:
                break
            right += 1
            s += right
        
        if right > n:
            break
        
        if s == n:
            answer += 1
        
        s -= left
        left += 1
    
    return answer